import getanalysis
import tradesim
import csv

trade_filepath = '../data/tradedata/Marubozu-Buy&Sell.csv'

with open(trade_filepath, 'rb') as trade_file:
    trade_array = []
    trade_file_data = csv.reader(trade_file, delimiter=',')
    for row in trade_file_data:
        trade_array.append(int(row[0]))

data_filepath = '../data/jcandles.csv'
        
data = getanalysis.import_j_candles(data_filepath)

[profit, profit_array] = tradesim.sim_trade(data, trade_array)
percent_profit = (profit - 1) * 100
print('Marubozu')
print('Profit: ' + str(percent_profit) + '%')
print('Max profit: ' + str((max(profit_array)-1)*100) + '%\n')