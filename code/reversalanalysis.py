import getanalysis
import tradesim

# Import japanese candle data
data = getanalysis.import_j_candles('../data/jcandles.csv')

# Get all sorts of data
[increase_data, body_sizes, shadow_sizes, data_length, run_length_data, reversals] = getanalysis.analyse(data)

# Get body size data
[av_body_size, body_size_quartiles] = getanalysis.body_size_analysis(body_sizes)

# Get Dojis
doji_array = [0]*data_length
for i in range(data_length):
    if body_sizes[i] < body_size_quartiles[1]:
        doji_array[i] += 1
        
###########
# Testing #
###########

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
print('Max profit: ' + str(max(profit_array)) + '%\n')


# Buy at Doji reversal, sell at reversal
trade_array = [0]*data_length
last_trade = 0
for i in range(data_length):
    # Reversal
    if run_length_data[i] == 0:
        # Gain
        if increase_data[i] == 1:
            # Sold last
            if last_trade == 0:
                # Doji
                if doji_array[i] == 1:
                    #Buy
                    trade_array[i] = 1
                    last_trade = 1
        # Loss
        else:
            # Bought last
            if last_trade == 1:
                #Sell
                trade_array[i] = 2
                last_trade = 0
                
[profit, profit_array] = tradesim.sim_trade(data, trade_array)
percent_profit = (profit - 1) * 100
print('Buying at Doji reversal, selling at reversal')
print('Profit: ' + str(percent_profit) + '%')
print('Max profit: ' + str(max(profit_array)) + '%\n')