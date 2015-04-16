import sys
sys.path.append('./tools')

import getanalysis
import tradesim
import csv
import time
import numpy

# Import Japanese data
jdata_filepath = '../data/jcandles.csv'
jdata = getanalysis.import_j_candles(jdata_filepath)
[jincrease_data, jbody_sizes, jshadow_sizes, data_length] = getanalysis.body_and_shadow(jdata)
[jrun_length_data, jreversals] = getanalysis.runs_and_reversal(jdata, data_length, jincrease_data)
jrun_function_data = getanalysis.run_analysis(jbody_sizes, data_length, jrun_length_data, jincrease_data)

# Import Heikin Ashi data
hadata_filepath = '../data/hacandles.csv'
hadata = getanalysis.import_j_candles(hadata_filepath)
[haincrease_data, habody_sizes, hashadow_sizes, data_length] = getanalysis.body_and_shadow(hadata)
[harun_length_data, hareversals] = getanalysis.runs_and_reversal(hadata, data_length, haincrease_data)
harun_function_data = getanalysis.run_analysis(habody_sizes, data_length, harun_length_data, haincrease_data)

def calculateprofit(datadata, datalimits, combined_trade_array):
[jdata, data_length, body_sizes, shadow_sizes, body_shadow_ratios, reversals, increase_data, run_function_data] = datadata
[body_lim, shadow_lim, ratio_lim, prev_run_lim, prev_diff_lim] = datalimits
# 0 for sell, 1 for buy
last_trade = 0
trade_array = [0]*data_length
for i in range(datadata[1]):
    if (last_trade == 0):
        if ((reversals[i] == 1) and (increase_data[i] == 1) and
            (body_sizes[i] <= body_lim[1]) and (body_sizes[i] >= body_lim[0]) and
            (shadow_sizes[i] <= shadow_lim[1]) and (shadow_sizes[i] >= shadow_lim[0]) and
            (body_shadow_ratios[i] <= ratio_lim[1]) and (body_shadow_ratios[i] >= ratio_lim[0]) and
            (run_function_data[i][1] <= prev_run_lim[1]) and (run_function_data[i][1] >= prev_run_lim[0]) and
            (run_function_data[i][2] <= prev_diff_lim[1]) and (run_function_data[i][2] >= prev_diff_lim[0])):
                trade_array[i] += 1
                last_trade = 1
        elif (last_trade == 1):
            if (reversals[i] == 1):
                trade_array[i] += 2
                last_trade = 0
    [profit, profit_array] = tradesim.sim_trade(jdata, trade_array)
    if profit > 1:
        temp_combined_trade_array = [None] * data_length
        for i in range(data_length):
            if trade_array[i] > 0:
                temp_combined_trade_array[i] = trade_array[i]
        [com_profit, com_profit_array] = tradesim.sim_trade(jdata, combined_trade_array)
        [temp_profit, temp_profit_array] = tradesim.sim_trade(jdata, temp_combined_trade_array)
        if temp_profit > com_profit:
            combined_trade_array = temp_combined_trade_array
    return([profit, combined_trade_array])

# Code will iterate through each factor using either percentiles or values
# defined by values set in a controlling array
# Factors included are:
# Reversal - Body size, Shadow size, Body to shadow ratio
# Candle before reversal - Body size, Shadow size, Body to shadow ratio
# Run before reversal - Run length, Difference of values
# Candles in run before reversal - Average body size, Average shadow size
# Average body to shadow ratio

