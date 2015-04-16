import sys
sys.path.append('./tools')

import getanalysis
import tradesim_n
import tradesim
import csv
import time
import numpy
import pylab

# Import data
jdata_filepath = '../data/jcandles.csv'
hadata_filepath = '../data/hacandles.csv'
jdata = getanalysis.import_j_candles(jdata_filepath)
hadata = getanalysis.import_j_candles(hadata_filepath)

([jincrease_data, jbody_sizes, jshadow_sizes,
	data_length]) = getanalysis.body_and_shadow(jdata)
[jrun_length_data, jreversals] = getanalysis.runs_and_reversal(jdata,
	data_length, jincrease_data)

([haincrease_data, habody_sizes, hashadow_sizes,
	data_length]) = getanalysis.body_and_shadow(hadata)
[harun_length_data, hareversals] = getanalysis.runs_and_reversal(hadata,
	data_length, haincrease_data)

jrun_function_data = getanalysis.run_analysis(jbody_sizes, data_length,
	jrun_length_data, jincrease_data)
harun_function_data = getanalysis.run_analysis(habody_sizes, data_length,
	harun_length_data, haincrease_data)

jbody_shadow_ratios = [0]*data_length
habody_shadow_ratios = [0]*data_length
jrun_lengths = []
jrun_diffs = []
harun_lengths = []
harun_diffs = []
for i in range(data_length):
	if jshadow_sizes[i] > 0:
		jbody_shadow_ratios[i] = jbody_sizes[i]/jshadow_sizes[i]
	else:
		jbody_shadow_ratios[i] = 0
	if hashadow_sizes[i] > 0:
		habody_shadow_ratios[i] = habody_sizes[i]/hashadow_sizes[i]
	else:
		habody_shadow_ratios[i] = 0
	if jrun_function_data[i] <> None:
		jrun_lengths.append(jrun_function_data[i][3])
		jrun_diffs.append(jrun_function_data[i][4])
	if harun_function_data[i] <> None:
		harun_lengths.append(harun_function_data[i][3])
		harun_diffs.append(harun_function_data[i][4])

n_cents = 4
# Get percentiles of Japanese candle data
jbody_sizes_cents = getanalysis.getpercentiles(jbody_sizes, n_cents)
jshadow_sizes_cents = getanalysis.getpercentiles(jshadow_sizes, n_cents)
jbody_shadow_ratios_cents = getanalysis.getpercentiles(jbody_shadow_ratios, n_cents)
jrun_lengths_cents = getanalysis.getpercentiles(jrun_lengths, n_cents)
jrun_diffs_cents = getanalysis.getpercentiles(jrun_diffs, n_cents)

# Get percentiles of Heikin Ashi candle data
habody_sizes_cents = getanalysis.getpercentiles(habody_sizes, n_cents)
hashadow_sizes_cents = getanalysis.getpercentiles(hashadow_sizes, n_cents)
habody_shadow_ratios_cents = getanalysis.getpercentiles(habody_shadow_ratios, n_cents)
harun_lengths_cents = getanalysis.getpercentiles(harun_lengths, n_cents)
harun_diffs_cents = getanalysis.getpercentiles(harun_diffs, n_cents)

# Function to find what percentile range data fits into
def getcents(data, cents):
	cent_value = 0
	for i in range(len(cents)):
		if cents[i] >= data:
			# This is the percentile range above the one of data
			cent_value = i
			break
	return cent_value

# Function to create a buy/sell map from percentiles
def gettradedata(all_cents, coefficient_data, candle_data, reversal_data,
	this_iter):
	([body_sizes_cents, shadow_sizes_cents, body_shadow_ratios_cents,
		run_lengths_cents, run_diffs_cents]) = all_cents
	([i, this_climb_profit, this_climb_length, this_body_size,
		this_shadow_size, this_body_shadow_ratio, this_imm_prev_body_size,
		this_imm_prev_shadow_size, this_imm_prev_body_shadow_ratio,
		this_prev_run_length, this_prev_run_diff, this_prev_av_body_size,
		this_prev_av_shadow_size,
		this_prev_av_body_shadow_ratio]) = coefficient_data[this_iter]
	this_body_size_cent = getcents(float(this_body_size), body_sizes_cents)
	this_shadow_size_cent = getcents(float(this_shadow_size),
		shadow_sizes_cents)
	this_body_shadow_ratio_cent = getcents(float(this_body_shadow_ratio),
		body_shadow_ratios_cents)
	this_imm_prev_body_size_cent = getcents(float(this_imm_prev_body_size),
		body_sizes_cents)
	this_imm_prev_shadow_size_cent  = getcents(float(
		this_imm_prev_shadow_size), shadow_sizes_cents)
	this_imm_prev_body_shadow_ratio_cent = getcents(float(
		this_imm_prev_body_shadow_ratio), body_shadow_ratios_cents)
	this_prev_run_length_cent = getcents(float(this_prev_run_length),
		run_lengths_cents)
	this_prev_run_diff_cent = getcents(float(this_prev_run_diff),
		run_diffs_cents)
	this_prev_av_body_size_cent = getcents(float(this_prev_av_body_size),
		body_sizes_cents)
	this_prev_av_shadow_size_cent = getcents(float(this_prev_av_shadow_size),
		shadow_sizes_cents)
	this_prev_av_body_shadow_ratio_cent = getcents(float(
		this_prev_av_body_shadow_ratio), body_shadow_ratios_cents)
	# Blank list of trade instructions, 1 for buy, 2 for sell
	trade_data = [0]*len(candle_data)
	for k in range(len(coefficient_data)):
		([i, this_climb_profit, this_climb_length, this_body_size,
			this_shadow_size, this_body_shadow_ratio,
			this_imm_prev_body_size, this_imm_prev_shadow_size,
			this_imm_prev_body_shadow_ratio, this_prev_run_length,
			this_prev_run_diff, this_prev_av_body_size,
			this_prev_av_shadow_size,
			this_prev_av_body_shadow_ratio]) = coefficient_data[k]
		if ((float(this_body_size) >= body_sizes_cents[this_body_size_cent-1]) and
			(float(this_body_size) <= body_sizes_cents[this_body_size_cent]) and
			(float(this_shadow_size) >= shadow_sizes_cents[this_shadow_size_cent-1]) and
			(float(this_shadow_size) <= shadow_sizes_cents[this_shadow_size_cent]) and
			(float(this_body_shadow_ratio) >= body_shadow_ratios_cents[this_body_shadow_ratio_cent-1]) and
			(float(this_body_shadow_ratio) <= body_shadow_ratios_cents[this_body_shadow_ratio_cent]) and
			(float(this_imm_prev_body_size) >= body_sizes_cents[this_imm_prev_body_size_cent-1]) and
			(float(this_imm_prev_body_size) <= body_sizes_cents[this_imm_prev_body_size_cent]) and
			(float(this_imm_prev_shadow_size) >= shadow_sizes_cents[this_imm_prev_shadow_size_cent-1]) and
			(float(this_imm_prev_shadow_size) <= shadow_sizes_cents[this_imm_prev_shadow_size_cent]) and
			(float(this_imm_prev_body_shadow_ratio) >= body_shadow_ratios_cents[this_imm_prev_body_shadow_ratio_cent-1]) and
			(float(this_imm_prev_body_shadow_ratio) <= body_shadow_ratios_cents[this_imm_prev_body_shadow_ratio_cent]) and
			(float(this_prev_run_length) >= run_lengths_cents[this_prev_run_length_cent-1]) and
			(float(this_prev_run_length) <= run_lengths_cents[this_prev_run_length_cent]) and
			(float(this_prev_run_diff) >= run_diffs_cents[this_prev_run_diff_cent-1]) and
			(float(this_prev_run_diff) <= run_diffs_cents[this_prev_run_diff_cent]) and
			(float(this_prev_av_body_size) >= body_sizes_cents[this_prev_av_body_size_cent-1]) and
			(float(this_prev_av_body_size) <= body_sizes_cents[this_prev_av_body_size_cent]) and
			(float(this_prev_av_shadow_size) >= shadow_sizes_cents[this_prev_av_shadow_size_cent-1]) and
			(float(this_prev_av_shadow_size) <= shadow_sizes_cents[this_prev_av_shadow_size_cent]) and
			(float(this_prev_av_body_shadow_ratio) >= body_shadow_ratios_cents[this_prev_av_body_shadow_ratio_cent-1]) and
			(float(this_prev_av_body_shadow_ratio) <= body_shadow_ratios_cents[this_prev_av_body_shadow_ratio_cent])):
				trade_data[int(i)] = 1
	return trade_data

def combine_profits(first_trade_array, second_trade_array, second_n):
	if len(first_trade_array) == len(second_trade_array):
		data_length = len(first_trade_array)
		# Add sells to second array, n after buying
		for i1 in range(data_length):
			if second_trade_array[i1] == 1:
				try:
					second_trade_array[i1 + second_n] = 2
				except:
					pass
		# Combine arrays
		combined_trade_array = [0]*data_length
		for i in range(data_length):
			if combined_trade_array[i] == 0:
				if first_trade_array[i] > 0:
					combined_trade_array[i] = first_trade_array[i]
				if second_trade_array[i] > 0:
					combined_trade_array[i] = second_trade_array[i]
	return combined_trade_array

# Import organised coefficient data
# This is the data from all of the reversals from a decline to a climb
# The following code will iterate through each reversal, find the percentiles
# that match each reversal, and run a profit calculation funciton for the
# coefficients for each of the reversals to find pand combine profitable
# combinations of variables
jcoefficient_filepath = '../data/analysis/coefficientanalysis.csv'
hacoefficient_filepath = '../data/analysis/hacoefficientanalysis.csv'

jcoefficient_data = []
hacoefficient_data = []
# Open and read the csv files
with open(jcoefficient_filepath, 'rb') as jcoefficient_file:
    data = csv.reader(jcoefficient_file, delimiter=',')
    for row in data:
    	jcoefficient_data.append(row)
with open(hacoefficient_filepath, 'rb') as hacoefficient_file:
    data = csv.reader(hacoefficient_file, delimiter=',')
    for row in data:
    	hacoefficient_data.append(row)

# Find percentiles to test with
jco_length = len(jcoefficient_data)
haco_length = len(hacoefficient_data)

# Iterate through each reversal in each of the candle datasets, getting the
# percentile ranges and simulating buying and selling for each of the
# iterations
# Japanese data
n = 10
trade_data = [None]*jco_length
profit_data = [None]*jco_length
max_profit_data = [None]*len(profit_data)
max_sell_after = [None]*len(profit_data)
for jiter in range(jco_length):
	this_cents = ([jbody_sizes_cents, jshadow_sizes_cents,
		jbody_shadow_ratios_cents, jrun_lengths_cents, jrun_diffs_cents])
	trade_data[jiter] = gettradedata(this_cents, jcoefficient_data, jdata, jreversals,
		jiter)
	this_set = [None]*n
	for i in range(n):
		this_set[i] = tradesim_n.sim_trade(jdata, trade_data[jiter], i+1)
	profit_data[jiter] = this_set
	this_max_profit_data = max(this_set)
	this_max_sell_after = this_set.index(max(this_set))+1
	max_profit_data[jiter] = this_max_profit_data
	max_sell_after[jiter] = this_max_sell_after
combined_trade_array = [0]*data_length
this_profit = 1.0
for i in range(len(trade_data)):
	if max_profit_data[i] > 1.0:
		# Try adding trade data together to get more profit
		trial_combined_trade_array = combine_profits(combined_trade_array, trade_data[i], max_sell_after[i])
		trial_profit = tradesim.sim_trade(jdata, trial_combined_trade_array)
		if trial_profit > this_profit:
			this_profit = trial_profit
			combined_trade_array = trial_combined_trade_array
percent_profit = (this_profit - 1)*100
print('Japanese candles: ' + str(percent_profit) + '%')

# Heikin Ashi data
n = 20
trade_data = [None]*haco_length
profit_data = [None]*haco_length
max_profit_data = [None]*len(profit_data)
max_sell_after = [None]*len(profit_data)
for haiter in range(haco_length):
	this_cents = ([habody_sizes_cents, hashadow_sizes_cents,
		habody_shadow_ratios_cents, harun_lengths_cents, harun_diffs_cents])
	trade_data[haiter] = gettradedata(this_cents, hacoefficient_data, hadata, hareversals,
		haiter)
	this_set = [None]*n
	for i in range(n):
		this_set[i] = tradesim_n.sim_trade(jdata, trade_data[haiter], i+1)
	profit_data[haiter] = this_set
	this_max_profit_data = max(this_set)
	this_max_sell_after = this_set.index(max(this_set))+1
	max_profit_data[haiter] = this_max_profit_data
	max_sell_after[haiter] = this_max_sell_after
combined_trade_array = [0]*data_length
this_profit = 1.0
for i in range(len(trade_data)):
	if max_profit_data[i] > 1.0:
		# Try adding trade data together to get more profit
		trial_combined_trade_array = combine_profits(combined_trade_array, trade_data[i], max_sell_after[i])
		trial_profit = tradesim.sim_trade(jdata, trial_combined_trade_array)
		if trial_profit > this_profit:
			this_profit = trial_profit
			combined_trade_array = trial_combined_trade_array
percent_profit = (this_profit - 1)*100
print('Heikin Ashi candles: ' + str(percent_profit) + '%')