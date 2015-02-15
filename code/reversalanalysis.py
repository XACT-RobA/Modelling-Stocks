import csv

# Open & read the csv file
with open('../data/jcandles.csv', 'rb') as jcandle_file:
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
        
# Number of candles
data_length = len(data)

# Gain or loss
increase_data = [0]*data_length
# Iterate through candles
for i in range(data_length):
    # Get current open & close
    c_open = data[i][0]
    c_close = data[i][3]
    # Calculate body size
    body_size = c_close-c_open
    # Work out whether this candle is a gain or a loss
    this_increase = (body_size >= 0)
    # Flag candle as gain
    if this_increase:
        increase_data[i] += 1

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

