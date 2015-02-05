import csv

with open('../data/jcandles.csv', 'rb') as jcandle_file:
    data = []
    jcandle_data = csv.reader(jcandle_file, delimiter=',')
    for row in jcandle_data:
        j_open = float(row[1])
        j_close = float(row[4])
        data.append([j_open, j_close])

data_length = len(data)

increase_data = [None]*data_length
increase_bin = [0]*data_length

for i in range(data_length):
    c_open = data[i][0]
    c_close = data[i][1]
    body_size = c_close-c_open
    increase = (body_size >= 0)
    increase_data[i] = increase
    if increase:
        increase_bin[i] += 1

run_length_data = [None]*data_length

total_run_lengths = []

run_length = 0
for i in range(data_length):
    if i > 0:
        if increase_data[i] <> increase_data[i-1]:
            total_run_lengths.append(run_length-1)
            run_length = 0
    run_length_data[i] = run_length
    run_length += 1

max_run_length = max(total_run_lengths)
run_length_count = [0]*(max_run_length+1)
for i in range(len(total_run_lengths)):
    this_run_length = total_run_lengths[i]
    run_length_count[this_run_length] += 1

with open('../data/runlengths/allrunlengths.csv', 'wb') as allrunlengths_file:
    for i in range(len(run_length_data)):
        allrunlengths_file.write(str(run_length_data[i]) + ',' + str(increase_bin[i]) +  '\n')

with open('../data/runlengths/totalrunlengths.csv', 'wb') as totalrunlengths_file:
    for run_length in total_run_lengths:
        totalrunlengths_file.write(str(run_length) + '\n')

with open('../data/runlengths/runlengthscount.csv', 'wb') as runlengthscount_file:
    for i in range(len(run_length_count)):
        runlengthscount_file.write(str(run_length_count[i]) + ' runs of length ' + str(i) + '\n')

print('Run lengths calculated')
