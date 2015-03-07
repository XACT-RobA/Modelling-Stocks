import sys
sys.path.append('../tools')

import getanalysis
import tradesim
import csv

trade_filepath = '../../data/tradedata/spinningtopdata-trimmed.csv'

with open(trade_filepath) as trade_file:
    trade_array = []
    trade_file_data = csv.reader(trade_file, delimiter=',')
    for row in trade_file_data:
        trade_array.append(int(row[0]))

data_filepath = '../../data/jcandles.csv'
        
data = getanalysis.import_j_candles(data_filepath)

[profit, profit_array] = tradesim.sim_trade(data, trade_array)
percent_profit = (profit - 1) * 100
print('Spinning tops')
print('Profit: ' + str(percent_profit) + '%')
print('Max profit: ' + str(max(profit_array)) + '%\n')

[increase_data, body_sizes, shadow_sizes, data_length] = getanalysis.body_and_shadow(data)
