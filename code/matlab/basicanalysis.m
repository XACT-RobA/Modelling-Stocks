format long;

% To read in the Japanese candle data
filelocation = '../../data/jcandles.csv';
jc_file = fopen(filelocation, 'r');
j_candles = textscan(jc_file, '%d:%d %f %f %f %f', 'delimiter', ',', 'CollectOutput', 1);
fclose(jc_file);
j_time_temp = j_candles(1);
j_data_temp = j_candles(2);
j_time = j_time_temp{1};
j_data = j_data_temp{1};

% To read in the Heikin Ashi candle data
%filelocation = '../../data/hacandles.csv';
%hac_file = fopen(filelocation, 'r');
%ha_candles = textscan(hac_file, '%s %f %f %f %f', 'delimiter', ',', 'CollectOutput', 1);
%fclose(hac_file);
%ha_time_temp(1);
%ha_data_temp(2);
%ha_time = ha_time_temp{1};
%ha_data = ha_data_temp{1};


j_shadow_size = j_data(:,2)-j_data(:,3);
j_max_shadow_size = max(j_shadow_size);
j_min_shadow_size = min(j_shadow_size);
j_av_shadow_size = mean(j_shadow_size)
j_qu_shadow_size = quantile(j_shadow_size,5)

j_body_size = j_data(:,1)-j_data(:,4);
j_abs_body_size = abs(j_body_size);
j_max_body_size = max(j_abs_body_size);
j_av_body_size = mean(j_body_size)
j_qu_abs_body_size = quantile(j_abs_body_size,5)

j_gain = j_body_size>=0;
j_shadow_body_ratio = j_abs_body_size./j_shadow_size;
j_av_shadow_body_ratio = mean(j_shadow_body_ratio)
j_qu_shadow_body_ratio = quantile(j_shadow_body_ratio,5)


j_abs_body_size(500)
