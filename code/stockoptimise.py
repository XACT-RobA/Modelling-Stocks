import sys
sys.path.append('./tools')

import getanalysis
import tradesim
import csv
import time
import numpy

data_filepath = '../data/jcandles.csv'

data = getanalysis.import_j_candles(data_filepath)

[increase_data, body_sizes, shadow_sizes, data_length] = \
getanalysis.body_and_shadow(data)

# Have body sizes and shadow sizes

[run_length_data, reversals] = getanalysis.runs_and_reversal(data, data_length,
                                                             increase_data)

# Have reversals and run lengths

body_shadow_ratios = [0]*data_length
for i in range(data_length):
    try:
        body_shadow_ratios[i] += (body_sizes[i]/shadow_sizes[i])
    except:
        pass

run_function_data = [None]*data_length

run_diff_array = [0]*data_length
cumulative_run_length = 0
for i in range(data_length):
    if i == 0:
        cumulative_run_diff = 0
    cumulative_run_diff += body_sizes[i]
    run_diff_array[i] += cumulative_run_diff
    
prev_runs = []
prev_diffs = []
next_runs = []
next_diffs = []

for i in range(data_length):
    if run_length_data[i] == 0:
        prev_run_length = 0
        prev_run_diff = 0
        if i > 0:
            prev_run_length = run_length_data[i-1] + 1
            prev_run_diff = run_diff_array[i-1]
        next_run_length = 0
        next_run_diff = 0
        for j in range(max(run_length_data) - 1):
            k = j + 1
            if (i+k) < data_length:
                if run_length_data[i+k] == 0:
                    next_run_length = run_length_data[i+j]
                    next_run_diff = run_diff_array[i+j]
                    break
        if increase_data[i] == 1:
            run_function_data[i] = [i, prev_run_length, prev_run_diff,
                                    next_run_length, next_run_diff]
            prev_runs.append(prev_run_length)
            prev_diffs.append(prev_run_diff)
            next_runs.append(next_run_length)
            next_diffs.append(next_run_diff)
            
# Have all run lengths and gains/losses

def get_profit(datadata, datalimits):
    [data, data_length, body_sizes, shadow_sizes, body_shadow_ratios,
     reversals, increase_data, run_function_data] = datadata
    [body_lim, shadow_lim, ratio_lim, prev_run_lim, prev_diff_lim, next_run_lim,
     next_diff_lim] = datalimits
    # 0 for sell, 1 for buy
    last_trade = 0
    trade_array = [0]*data_length
    for i in range(datadata[1]):
        if (last_trade == 0):
            if ((reversals[i] == 1) and (increase_data[i] == 1) and
                (body_sizes[i] <= body_lim) and
                (shadow_sizes[i] <= shadow_lim) and
                (body_shadow_ratios[i] <= ratio_lim) and
                (run_function_data[i][1] >= prev_run_lim) and
                (run_function_data[i][2] >= prev_diff_lim) and
                (run_function_data[i][3] >= next_run_lim) and
                (run_function_data[i][4] >= next_diff_lim)):
                trade_array[i] += 1
                last_trade = 1
        elif (last_trade == 1):
            if (reversals[i] == 1):
                trade_array[i] += 2
                last_trade = 0
    [profit, profit_array] = tradesim.sim_trade(data,trade_array)
    return(profit)

starttime = time.time()

n_iter = 10

body_array = [0] * n_iter
shadow_array = [0] * n_iter
ratio_array = [0] * n_iter
prev_run_array = [0] * n_iter
prev_diff_array = [0] * n_iter
next_run_array = [0] * n_iter
next_diff_array = [0] * n_iter

for i in range(n_iter):
    p = ((i+1)*10)
    body_array[i] += numpy.percentile(body_sizes, p)
    shadow_array[i] += numpy.percentile(shadow_sizes, p)
    ratio_array[i] += numpy.percentile(body_shadow_ratios, p)
    prev_run_array[i] += numpy.percentile(prev_runs, p)
    prev_diff_array[i] += numpy.percentile(prev_diffs, p)
    next_run_array[i] += numpy.percentile(next_runs, p)
    next_diff_array[i] += numpy.percentile(next_diffs, p)

datadata = [data, data_length, body_sizes, shadow_sizes, body_shadow_ratios,
            reversals, increase_data, run_function_data]

profit_array = []
profit_stuff_array = []

for body_i in range(n_iter):
    #print(str(body_i*10) + '%')
    #body_lim = body_array[body_i]
    for shadow_i in range(n_iter):
        print(str((body_i*10)+shadow_i) + '%')
        #shadow_lim = shadow_array[shadow_i]
        for ratio_i in range(n_iter):
            #ratio_lim = ratio_array[ratio_i]
            for prev_run_i in range(n_iter):
                #prev_run_lim = prev_run_array[prev_run_i]
                for prev_diff_i in range(n_iter):
                    #prev_diff_lim = prev_diff_array[prev_diff_i]
                    for next_run_i in range(n_iter):
                        #next_run_lim = next_run_array[next_run_i]
                        for next_diff_i in range(n_iter):
                            #next_diff_lim = next_diff_array[next_diff_i]
                            datalimits = [body_array[body_i], shadow_array[shadow_i],
                                          ratio_array[ratio_i], prev_run_array[prev_run_i],
                                          prev_diff_array[prev_diff_i], next_run_array[next_run_i],
                                          next_diff_array[next_diff_i]]
                            this_profit =  get_profit(datadata, datalimits)
                            profit_array.append(this_profit)
                            profit_stuff_array.append([datalimits])
print('100%')

endtime = time.time()

timetaken = endtime-starttime
print(str(timetaken) + 's')

print(max(profit_array))