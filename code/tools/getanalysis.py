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
        this_shadow_size = c_high-c_close
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
    