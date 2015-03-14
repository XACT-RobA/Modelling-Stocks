format long

% Read in japanese candle data
filelocation = '../../data/jcandles.csv';
jc_file = fopen(filelocation, 'r');
j_candles = textscan(jc_file, '%d:%d %f %f %f %f', 'delimiter', ',', 'CollectOutput', 1);
fclose(jc_file);
data_temp = j_candles(2);
data = data_temp{1};

% Read in trade data csv
trade_filelocation = '../../data/tradedata/dojireversals.csv';
trade_file = fopen(trade_filelocation, 'r');
trade_file_data = textscan(trade_file, '%d8');
fclose(trade_file);
trade_array = trade_file_data{1};

% Get profit
[profit, profit_array] = tradesim(data, trade_array);

% Display percentage profit
disp('Buying at doji reversals')
percentage_profit = (profit-1)*100
max_profit = (max(profit_array)-1)/100
