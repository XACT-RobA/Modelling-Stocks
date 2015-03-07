import csv

# Open and read the csv file
with open('../../data/jcandles.csv', 'rb') as jcandle_file:
    data = []
    jcandle_data = csv.reader(jcandle_file, delimiter=',')
    for row in jcandle_data:
        # Using standard open-high-low-close stock data
        j_time = row[0]
        j_open = float(row[1])
        j_high = float(row[2])
        j_low = float(row[3])
        j_close = float(row[4])
        data.append([j_time, j_open, j_high, j_low, j_close])

# Convert the data to Heikin Ashi candles
data_length = len(data)
ha_data = [None]*data_length

for i in range(data_length):
    this_data = data[i]
    j_time = this_data[0]
    j_open = this_data[1]
    j_high = this_data[2]
    j_low = this_data[3]
    j_close = this_data[4]
    
    if i == 0:
        # First candle, calculate Heiken Ashi candle differently
        ha_open = round(((j_open+j_close)/2), 5)
        ha_high = j_high
        ha_low = j_low
        ha_close = round(((j_open+j_high+j_low+j_close)/4), 5)
    else:
        prev_data = ha_data[i-1]
        prev_ha_open = prev_data[1]
        prev_ha_close = prev_data[4]
        
        ha_open = round(((prev_ha_open+prev_ha_close)/2), 5)
        ha_close = round(((j_open+j_high+j_low+j_close)/4), 5)
        ha_high = max([j_high, ha_open, ha_close])
        ha_low = min([j_low, ha_open, ha_close])
    
    this_ha_candle = [j_time, ha_open, ha_high, ha_low, ha_close]
    ha_data[i] = this_ha_candle
    
with open('../../data/hacandles.csv', 'wb') as hacandle_file:
    ha_writer = csv.writer(hacandle_file, delimiter=',')
    for ha_candle in ha_data:
        ha_writer.writerow(ha_candle)
