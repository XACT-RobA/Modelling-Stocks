import getanalysis
import tradesim
import csv

filepath = '../data/jcandles.csv'

data = getanalysis.import_j_candles(filepath)

[increase_data, body_sizes, shadow_sizes, data_length, run_length_data, reversals] = getanalysis.analyse(data)

run_function_data = [None]*data_length

for i in range(data_length):
    if run_length_data[i] == 0:
        prev_run_length = 0
        prev_run_diff = 0
        if i > 0:
            try:
                prev_run_length = run_length_data[i-1] + 1
                prev_run_diff = sum(body_sizes[(i-(prev_run_length+1)):(i-1)])
            except:
                pass
        if i < data_length - 1:
            next_run_length = 0
            next_run_diff = 0
            try:
                j = 1
                while j < max(run_length_data) + 1:
                    if run_length_data[i+j] == 0:
                        next_run_length = run_length_data[i+j-1] + 1
                        next_run_diff = sum(body_sizes[i:(i+next_run_length - 1)])
                        j = max(run_length_data) + 1
                    j += 1
            except:
                pass
    
        run_function_data[i] = [i, prev_run_length, prev_run_diff, next_run_length, next_run_diff]

with open('../data/run_function_data.csv', 'wb') as run_data_file:
    run_data_writer = csv.writer(run_data_file, delimiter=',')
    for run_data in run_function_data:
        try:
            run_data_writer.writerow(run_data)
        except:
            pass
