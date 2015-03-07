import sys
sys.path.append('../tools')

import getanalysis
import tradesim
import csv

trade_filepath = '../../data/tradedata/Heikenashispintopsbuyorsell.csv'

with open(trade_filepath, 'rb') as trade_file:
    trade_array = []
    trade_file_data = csv.reader(trade_file, delimiter=',')
    for row in trade_file_data:
        trade_array.append(int(row[0]))

data_filepath = '../../data/hacandles.csv'
        
data = getanalysis.import_j_candles(data_filepath)

[profit, profit_array] = tradesim.sim_trade(data, trade_array)
percent_profit = (profit - 1) * 100
print('Heikin Ashi spinning tops')
print('Profit: ' + str(percent_profit) + '%')
print('Max profit: ' + str((max(profit_array)-1)*100) + '%\n')

trade_filepath = '../../data/tradedata/ha-candles-bear-and-bull-dojis.csv'
with open(trade_filepath, 'rb') as trade_file:
    trade_array = []
    trade_file_data = csv.reader(trade_file, delimiter=',')
    for row in trade_file_data:
        trade_array.append(int(row[0]))
[profit, profit_array] = tradesim.sim_trade(data, trade_array)
percent_profit = (profit - 1) * 100
print('Heikin Ashi dojis')
print('Profit: ' + str(percent_profit) + '%')
print('Max profit: ' + str((max(profit_array)-1)*100) + '%\n')
