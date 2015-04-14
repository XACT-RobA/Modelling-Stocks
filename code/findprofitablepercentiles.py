import sys
sys.path.append('./tools')

import getanalysis
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

# Get percentiles of Japanese candle data
jbody_sizes_cents = getanalysis.getpercentiles(jbody_sizes)
jshadow_sizes_cents = getanalysis.getpercentiles(jshadow_sizes)
jbody_shadow_ratios_cents = getanalysis.getpercentiles(jbody_shadow_ratios)
jrun_lengths_cents = getanalysis.getpercentiles(jrun_lengths)
jrun_diffs_cents = getanalysis.getpercentiles(jrun_diffs)

# Get percentiles of Heikin Ashi candle data
habody_sizes_cents = getanalysis.getpercentiles(habody_sizes)
hashadow_sizes_cents = getanalysis.getpercentiles(hashadow_sizes)
habody_shadow_ratios_cents = getanalysis.getpercentiles(habody_shadow_ratios)
harun_lengths_cents = getanalysis.getpercentiles(harun_lengths)
harun_diffs_cents = getanalysis.getpercentiles(harun_diffs)

# Function to find what percentile range data fits into
def getcents(data, cents):
	cent_value = 0
	for i in range(len(cents)):
		if cents[i] >= data:
			# This is the percentile range above the one of data
			cent_value = i
			break
	return cent_value

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
for jiter in range(jco_length):
	([i, this_climb_profit, this_climb_length, this_body_size,
		this_shadow_size, this_body_shadow_ratio, this_imm_prev_body_size,
		this_imm_prev_shadow_size, this_imm_prev_body_shadow_ratio,
		this_prev_run_length, this_prev_run_diff, this_prev_av_body_size,
		this_prev_av_shadow_size, this_prev_av_body_shadow_ratio]
		) = jcoefficient_data[jiter]
	this_body_size_cent = getcents(float(this_body_size), jbody_sizes_cents)
	this_shadow_size_cent = getcents(float(this_shadow_size),
		jshadow_sizes_cents)
	this_body_shadow_ratio_cent = getcents(float(this_body_shadow_ratio),
		jbody_shadow_ratios_cents)
	this_imm_prev_body_size_cent = getcents(float(this_imm_prev_body_size),
		jbody_sizes_cents)
	this_imm_prev_shadow_size_cent  = getcents(float(
		this_imm_prev_shadow_size), jshadow_sizes_cents)
	this_imm_prev_body_shadow_ratio_cent = getcents(float(
		this_imm_prev_body_shadow_ratio), jbody_shadow_ratios_cents)
	this_prev_run_length_cent = getcents(float(this_prev_run_length),
		jrun_lengths_cents)
	this_prev_run_diff_cent = getcents(float(this_prev_run_diff),
		jrun_diffs_cents)
	this_prev_av_body_size_cent = getcents(float(this_prev_av_body_size),
		jbody_sizes_cents)
	this_prev_av_shadow_size_cent = getcents(float(this_prev_av_shadow_size),
		jshadow_sizes_cents)
	this_prev_av_body_shadow_ratio_cent = getcents(float(
		this_prev_av_body_shadow_ratio), jbody_shadow_ratios_cents)
	for j in range(jco_length):
		pass
		#
		#
		#
		#


for haiter in range(haco_length):
	([i, his_climb_profit, this_climb_length, this_body_size, this_shadow_size,
	this_body_shadow_ratio, this_imm_prev_body_size, this_imm_prev_shadow_size,
	this_imm_prev_body_shadow_ratio, this_prev_run_length, this_prev_run_diff,
	this_prev_av_body_size, this_prev_av_shadow_size,
	this_prev_av_body_shadow_ratio]) = hacoefficient_data[haiter]
	this_body_size_cent = getcents(float(this_body_size), habody_sizes_cents)
	this_shadow_size_cent = getcents(float(this_shadow_size),
		hashadow_sizes_cents)
	this_body_shadow_ratio_cent = getcents(float(this_body_shadow_ratio),
		habody_shadow_ratios_cents)
	this_imm_prev_body_size_cent = getcents(float(this_imm_prev_body_size),
		habody_sizes_cents)
	this_imm_prev_shadow_size_cent  = getcents(float(
		this_imm_prev_shadow_size), hashadow_sizes_cents)
	this_imm_prev_body_shadow_ratio_cent = getcents(float(
		this_imm_prev_body_shadow_ratio), habody_shadow_ratios_cents)
	this_prev_run_length_cent = getcents(float(this_prev_run_length),
		harun_lengths_cents)
	this_prev_run_diff_cent = getcents(float(this_prev_run_diff),
		harun_diffs_cents)
	this_prev_av_body_size_cent = getcents(float(this_prev_av_body_size),
		habody_sizes_cents)
	this_prev_av_shadow_size_cent = getcents(float(this_prev_av_shadow_size),
		hashadow_sizes_cents)
	this_prev_av_body_shadow_ratio_cent = getcents(float(
		this_prev_av_body_shadow_ratio), habody_shadow_ratios_cents)