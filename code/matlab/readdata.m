format long;

%%% Reading the data


%% Japanese candles

% To read in the Japanese candle data
filelocation = '../../data/jcandles.csv';
jc_file = fopen(filelocation, 'r');
j_candles = textscan(jc_file, '%d:%d %f %f %f %f', 'delimiter', ',', 'CollectOutput', 1);
fclose(jc_file);
j_time = j_candles(1){1};
j_data = j_candles(2){1};


%% Heikin Ashi candles

% To read in the Heikin Ashi candle data
filelocation = '../../data/hacandles.csv';
hac_file = fopen(filelocation, 'r');
ha_candles = textscan(hac_file, '%s %f %f %f %f', 'delimiter', ',', 'CollectOutput', 1);
fclose(hac_file);
ha_time = ha_candles(1){1};
ha_data = ha_candles(2){1};


%%% Using the data

% To get the first Japanese candle
j_data(1,:)

% To get the thrid Japanese candle
j_data(3,:)

% To get the time for the third candle
j_time(3,:)

% To get the open price for the first Heikin Ashi candle
ha_data(1,1)

% To get the close price for the first Heikin Ashi candle
ha_data(1,4)
