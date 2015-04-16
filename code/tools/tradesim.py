def sim_trade(data, trade_array):
    data_length = len(data)
    if data_length == len(trade_array):
        value = 1.0
        last_trade = 0
        buy_price = 0
        sell_price = 0
        profit_array = [0] * data_length
        for i in range(data_length):
            # Buy and sell at the closing price
            if trade_array[i] == 1:
                # Buy
                # Check not already bought
                if last_trade == 0:
                    buy_price = data[i][3]
                    last_trade = 1
            elif trade_array[i] == 2:
                # Sell
                # Check not already sold
                if last_trade == 1:
                    sell_price = data[i][3]
                    value = ((((value * (sell_price / buy_price))-1)/1)+1)
                    profit_array[i] += value
                    last_trade = 0
        #return [value, profit_array]
        return value
    else:
        print('Error: Data and trade array are different lengths')
        #return [0, 0]
        return 0
    
def save_trade_array(trade_array, filepath):
    with open(filepath, 'wb') as trade_file:
        for trade_value in trade_array:
            trade_file.write(str(trade_value) + '\n')
        print('Trade array saved')