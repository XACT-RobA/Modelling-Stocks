import getanalysis
import tradesim

data = getanalysis.import_j_candles('../data/jcandles.csv')

[increase_data, body_sizes, shadow_sizes, data_length, run_length_data, reversals] = getanalysis.analyse(data)


############

# Buy or sell on every reversal

trade_array = [0]*data_length
last_trade = 0

for i in range(data_length):
    if i == 0:
        if increase_data[i] == 1:
            # Buy
            trade_array[i] = 1
            last_trade = 1
    else:
        if run_length_data[i] == 0:
            trade_array[i] = last_trade + 1
            last_trade = (last_trade + 1) % 2
            
[profit, profit_array] = tradesim.sim_trade(data, trade_array)
percent_profit = (profit - 1) * 100
print('Buying and selling every reversal')
print('Profit: ' + str(percent_profit) + '%')
print('Max profit: ' + str(max(profit_array)) + '%')