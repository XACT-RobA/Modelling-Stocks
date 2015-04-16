import csv
import numpy

def import_j_candles(filepath):
    # Open & read the csv file
    with open(filepath, 'rb') as jcandle_file:
        data = []
        # Read the csv file
        jcandle_data = csv.reader(jcandle_file, delimiter=',')
        # Iterate through the rows
        for row in jcandle_data:
            # Using standard open-high-low-close stock data
            j_open = float(row[1])
            j_high = float(row[2])
            j_low = float(row[3])
            j_close = float(row[4])
            # Store the data
            data.append([j_open, j_high, j_low, j_close])
    return data

def body_and_shadow(data):
    # Number of candles
    data_length = len(data)
    # Gain or loss
    increase_data = [0]*data_length
    # Body sizes
    body_sizes = [0]*data_length
    # Shadow sizes
    shadow_sizes = [0]*data_length
    # Iterate through candles
    for i in range(data_length):
        # Get current open & close
        c_open = data[i][0]
        c_high = data[i][1]
        c_low = data[i][2]
        c_close = data[i][3]
        # Calculate body size
        this_body_size = c_close-c_open
        # Store body sizes
        body_sizes[i] += abs(this_body_size)
        # Work out whether this candle is a gain or a loss
        this_increase = (this_body_size >= 0)
        # Flag candle as gain
        if this_increase:
            increase_data[i] += 1
        # Calculate shadow size
        this_shadow_size = c_high-c_low
        shadow_sizes[i] += this_shadow_size
    return ([increase_data, body_sizes, shadow_sizes, data_length])

def runs_and_reversal(data, data_length, increase_data):
    # Get run lengths & reversals
    run_length_data = [None]*data_length
    run_length = 0
    reversals = [0]*data_length
    # Iterate through candles
    for i in range(data_length):
        # Set first candle as 0
        if i > 0:
            # If reversal
            if increase_data[i] <> increase_data[i-1]:
                # Reset run length
                run_length = 0
                # Flag reversal
                reversals[i] += 1
        # Set current run length
        run_length_data[i] = run_length
        # Iterate
        run_length += 1
    return ([run_length_data, reversals])

def analyse(data):
    [increase_data, body_sizes, shadow_sizes, data_length] = body_and_shadow(data)
    [run_length_data, reversals] = runs_and_reversal(data, data_length, increase_data)
    return ([increase_data, body_sizes, shadow_sizes, data_length, run_length_data, reversals])

def size_analysis(sizes):
    av_size = numpy.mean(sizes)
    min_size = min(sizes)
    lower_qu_size = numpy.percentile(sizes, 25)
    median_size = numpy.percentile(sizes, 50)
    upper_qu_size = numpy.percentile(sizes, 75)
    max_size = max(sizes)
    return([av_size,[min_size, lower_qu_size, median_size, upper_qu_size, max_size]])

def body_size_analysis(body_sizes):
    return size_analysis(body_sizes)
    
def shadow_size_analysis(shadow_sizes):
    return size_analysis(shadow_sizes)
    
def body_shadow_ratio_analysis(body_sizes, shadow_sizes):
    body_shadow_ratios = [0]*len(body_sizes)
    for i in range(len(body_sizes)):
        body_shadow_ratios[i] += (body_sizes[i]/shadow_sizes[i])
    return size_analysis(body_shadow_ratios)

def run_analysis(body_sizes, data_length, run_length_data, increase_data):
    run_diff_array = [None]*data_length
    current_run_diff = 0
    current_increase_value = 2
    prev_run_length = 0
    prev_run_diff = 0
    run_length_iter = 0
    run_diff_iter = 0
    for i in range(data_length):
        if current_increase_value <> increase_data[i]:
            for j in range(max(run_length_data)):
                if (i+j) < data_length:
                    if increase_data[i+j] <> increase_data[i]:
                        # End of run
                        next_run_length = run_length_iter
                        next_run_diff = run_diff_iter
                        run_length_iter = 0
                        run_diff_iter = 0
                        break
                    run_length_iter += 1
                    run_diff_iter += body_sizes[i+j]
                else:
                    next_run_length = 0
                    next_run_diff = 0
            run_diff_array[i] = [i, prev_run_length, prev_run_diff, next_run_length, next_run_diff]
            prev_run_length = 0
            prev_run_diff = 0
            current_increase_value = increase_data[i]
        prev_run_length += 1
        prev_run_diff += body_sizes[i]
    return run_diff_array
        
# Function to get all 10th percentiles of data
def getpercentiles(data, n):
    this_percentiles = []
    for i in range(n+1):
        this_percentiles.append(numpy.percentile(data, i*(100/n)))
    '''
    this_percentiles = ([numpy.percentile(data, 0),
        numpy.percentile(data,10), numpy.percentile(data,20),
        numpy.percentile(data,30), numpy.percentile(data,40),
        numpy.percentile(data,50), numpy.percentile(data,60),
        numpy.percentile(data,70), numpy.percentile(data,80),
        numpy.percentile(data,90), numpy.percentile(data,100)])
    '''
    return this_percentiles