function [value, profit_array] = tradesim(data, trade_array)
    data_length = max(size(data));
    trade_array_length = max(size(trade_array));
    if data_length == trade_array_length
        value = 1;
        last_trade = 0;
        buy_price = 0;
        sell_price = 0;
        profit_array = zeros(data_length, 1);
        for i = 1:data_length
            % Buy and sell at the closing price
            if trade_array(i) == 1
                % Buy
                % Check not already bought
                if last_trade == 0
                    buy_price = data(i, 4);
                    last_trade = 1;
                end
            elseif trade_array(i) == 2
                % Sell
                % Check not already sold
                if last_trade == 1
                    sell_price = data(i, 4);
                    value = value * (sell_price / buy_price);
                    profit_array(i) = profit_array(i) + value;
                    last_trade = 0;
                end
            end
        end
    end
return
