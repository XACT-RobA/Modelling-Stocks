def sim_trade(data, trade_array, sell_after):
    data_length = len(data)
    if data_length == len(trade_array):
        value = 1.0
        last_trade = 0
        buy_price = 0
        sell_price = 0
        buy_i = 0
        profit_array = [0] * data_length
        for i in range(data_length):
            # Buy and sell at the closing price
            # Check not already bought
            if last_trade == 0:
                # Buy
                if trade_array[i] == 1:
                    buy_price = data[i][3]
                    buy_i = i
                    last_trade = 1
            # Check not already sold
            elif last_trade == 1:
                # Sell
                if (i == (buy_i+sell_after)):
                    sell_price = data[i][3]
                    value = value * (sell_price / buy_price)
                    profit_array[i] += value
                    last_trade = 0
        #return [value, profit_array]
        return value
    else:
        print('Error: Data and trade array are different lengths')
        return 0
    
def save_trade_array(trade_array, filepath):
    with open(filepath, 'wb') as trade_file:
        for trade_value in trade_array:
            trade_file.write(str(trade_value) + '\n')
        print('Trade array saved')