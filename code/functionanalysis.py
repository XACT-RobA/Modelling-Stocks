import getanalysis
import tradesim
import csv

filepath = '../data/jcandles.csv'

data = getanalysis.import_j_candles(filepath)

[increase_data, body_sizes, shadow_sizes, data_length, run_length_data, reversals] = getanalysis.analyse(data)

run_function_data = [None]*data_length

run_diff_array = [0]*data_length
cumulative_run_length = 0
for i in range(data_length):
    if i == 0:
        cumulative_run_diff = 0
    cumulative_run_diff += body_sizes[i]
    run_diff_array[i] += cumulative_run_diff
    
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
'''
        run_function_data[i] = [i, prev_run_length, prev_run_diff, next_run_length, next_run_diff, increase_data[i]]
    else:
        run_function_data[i] = [0, 0, 0, 0, 0, increase_data[i]]

with open('../data/run_function_data.csv', 'wb') as run_data_file:
    run_data_writer = csv.writer(run_data_file, delimiter=',')
    for run_data in run_function_data:
        try:
            run_data_writer.writerow(run_data)
        except:
            pass        
'''

        if increase_data[i] == 1:
            run_function_data[i] = [i, prev_run_length, prev_run_diff, next_run_length, next_run_diff]

with open('../data/gain_function_data.csv', 'wb') as run_data_file:
    run_data_writer = csv.writer(run_data_file, delimiter=',')
    for run_data in run_function_data:
        try:
            run_data_writer.writerow(run_data)
        except:
            pass