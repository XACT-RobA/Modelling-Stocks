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
for i in range(data_length):
	if jshadow_sizes[i] > 0:
		jbody_shadow_ratios[i] = jbody_sizes[i]/jshadow_sizes[i]
	else:
		jbody_shadow_ratios[i] = 0

habody_shadow_ratios = [0]*data_length
for i in range(data_length):
	if hashadow_sizes[i] > 0:
		habody_shadow_ratios[i] = habody_sizes[i]/hashadow_sizes[i]
	else:
		habody_shadow_ratios[i] = 0

# Get percentiles of Japanese candle data
jbody_sizes_cents = getanalysis.getpercentiles(jbody_sizes)
jshadow_sizes_cents = getanalysis.getpercentiles(jshadow_sizes)
jbody_shadow_ratios_cents = getanalysis.getpercentiles(jbody_shadow_ratios)

# Get percentiles of Heikin Ashi candle data
habody_sizes_cents = getanalysis.getpercentiles(habody_sizes)
hashadow_sizes_cents = getanalysis.getpercentiles(hashadow_sizes)
habody_shadow_ratios_cents = getanalysis.getpercentiles(habody_shadow_ratios)

# Import organised coefficient data
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

for jiter in range(jco_length):
	([i, his_climb_profit, this_climb_length, this_body_size, this_shadow_size,
	this_body_shadow_ratio, this_imm_prev_body_size, this_imm_prev_shadow_size,
	this_imm_prev_body_shadow_ratio, this_prev_run_length, this_prev_run_diff,
	this_prev_av_body_size, this_prev_av_shadow_size,
	this_prev_av_body_shadow_ratio]) = jcoefficient_data[jiter]

for haiter in range(haco_length):
	([i, his_climb_profit, this_climb_length, this_body_size, this_shadow_size,
	this_body_shadow_ratio, this_imm_prev_body_size, this_imm_prev_shadow_size,
	this_imm_prev_body_shadow_ratio, this_prev_run_length, this_prev_run_diff,
	this_prev_av_body_size, this_prev_av_shadow_size,
	this_prev_av_body_shadow_ratio]) = hacoefficient_data[haiter]