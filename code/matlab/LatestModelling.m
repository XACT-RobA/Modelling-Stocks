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
j_av_shadow_size = mean(j_shadow_size);
j_qu_shadow_size = quantile(j_shadow_size,5);

j_body_size = j_data(:,1)-j_data(:,4);
j_abs_body_size = abs(j_body_size);
j_max_body_size = max(j_abs_body_size);
j_av_body_size = mean(j_body_size);
j_qu_abs_body_size = quantile(j_abs_body_size,5);

j_gain = j_body_size>=0;
j_shadow_body_ratio = j_abs_body_size./(j_shadow_size-j_abs_body_size);
j_av_shadow_body_ratio = mean(j_shadow_body_ratio);
j_qu_shadow_body_ratio = quantile(j_shadow_body_ratio,5);


j_abs_body_size(500);

j_body_size = j_data(:,1)-j_data(:,4);
j_abs_body_size = abs(j_body_size);
bodysizes = abs(j_data(:,1)-j_data(:,4));
shadowsize= j_data(:,2)- j_data(:,3);
totalDojiSta=0;
totalDMS=0;
totalDES=0;
totalDojiStar=0;
totalDFDoji=0;
totalGSDoji=0;
for i=1:5000
    if j_data(i,1) == j_data(i,4)
        upper_shadow(i)=j_data(i,2)-j_data(i,4);
        lower_shadow(i)=j_data(i,1)-j_data(i,3);
        shadow_ratio(i)=upper_shadow(i)./lower_shadow(i);
        if shadow_ratio(i) >= 0.8 && shadow_ratio(i) <= 1.2
            disp('DOJI STAR')
            i
            totalDojiStar=totalDojiStar+1;
        elseif shadow_ratio == 0
            if upper_shadow == 0
                disp('DRAGON FLY DOJI')
                i
                totalDFDoji=totalDFDoji+1;
            elseif lower_shadow == 0
                disp('GRAVE-STONE DOJI')
                i
                totalGSDoji=totalGSDoji+1;
            end
        end
    end
end
totalBeST=0;
totalBeIHang=0;
totalBeHang=0;
totalBeDoji=0;
for i=1:5000
    if j_data(i,1) > j_data(i,4)
        bear_upper_shadow(i)=j_data(i,2)-j_data(i,1);
        bear_lower_shadow(i)=j_data(i,4)-j_data(i,3);
        bear_body_size(i)=j_data(i,1)-j_data(i,4);
        if j_shadow_body_ratio(i) < 0.3 &&  j_shadow_body_ratio(i) > 0.1
        bear_shadow_ratio(i)=bear_upper_shadow(i)./bear_lower_shadow(i);
        if bear_shadow_ratio(i) >= 0.8 && bear_shadow_ratio(i) <= 1.2
            disp('BEAR SPINNING TOP');
            i
            totalBeST=totalBeST+1;
        elseif bear_shadow_ratio(i) >= 5
            disp('BEAR INVERTED HANGING MAN (SHOOTING STAR)');
            i
            totalBeIHang=totalBeIHang+1;
        elseif bear_shadow_ratio(i) >= 0.2
            disp('BEAR HANGING MAN');
            i
            totalBeHang=totalBeHang+1;
        end
    end
    end
end
totalBuST=0;
totalBuH=0;
totalBuIH=0;
totalBuDoji=0;
for i=1:5000
    if j_data(i,4) > j_data(i,1)
        bull_upper_shadow(i)=j_data(i,2)-j_data(i,4);
        bull_lower_shadow(i)=j_data(i,1)-j_data(i,3);
        bull_body_size(i)=j_data(i,4)-j_data(i,1);
        if j_shadow_body_ratio(i) < 0.3 && j_shadow_body_ratio(i) > 0.1
        bull_shadow_ratio(i)=bull_upper_shadow(i)./bull_lower_shadow(i);
        if bull_shadow_ratio(i) >= 0.8 && bull_shadow_ratio(i) <= 1.2
            disp('BULL SPINNING TOP')
            i
            totalBuST=totalBuST+1;
        elseif bull_shadow_ratio(i) == 0
            if bull_upper_shadow(i) == 0
                disp('BULL HAMMER')
                i
                totalBuH=totalBuH+1;
            elseif bull_lower_shadow(i) == 0
                disp('BULL INVERTED HAMMER')
                i
                totalBuIH=totalBuIH+1;
            end
        end
    end
    end
end
totalBuMaru=0;
totalBeMaru=0;

for i=1:5000
    if j_data(i,1) == j_data(i,2) && j_data(i,3) == j_data(i,4)
        disp('BEAR MARUBOZU')
        i
        totalBeMaru=totalBeMaru+1;
    elseif j_data(i,4) == j_data(i,2) && j_data(i,3) == j_data(i,1)
        disp('BULL MARUBOZU')
        i
        totalBuMaru=totalBuMaru+1;
    end
end
totalDFDoji
totalGSDoji
totalDojiStar
totalDojiSta
totalBeST
totalBeHang
totalBeIHang
totalBeDoji
totalBuST
totalBuH
totalBuIH
totalBuDoji
totalBuMaru
totalBeMaru
totalBuDES=0;
totalBeDES=0;
totalBuDMS=0;
totalBeDMS=0;
totalDSES=0;
totalDSMS=0;
totalDojiSta=0;
totalBeDoji=0;
totalBuDoji=0;
for i = 1:5000
   if bodysizes(i) == 0
       upper_shadow(i)=j_data(i,2)-j_data(i,1);
       lower_shadow(i)=j_data(i,4)-j_data(i,3);
       shadow_ratio(i)=upper_shadow(i)./lower_shadow(i);
       if shadow_ratio(i) >= 0.8 && shadow_ratio(i) <= 1.2
       disp('DOJI STAR')
       i
       totalDojiSta=totalDojiSta+1;
       if j_data(i-1,1) > j_data(i-1,4)
        bear_upper_shadow(i-1)=j_data(i-1,2)-j_data(i-1,1);
        bear_lower_shadow(i-1)=j_data(i-1,4)-j_data(i-1,3);
        bear_body_size(i-1)=j_data(i-1,1)-j_data(i-1,4);
        bear_shadow_body_ratio(i-1) = bear_body_size(i-1)./(bear_upper_shadow(i-1)+bear_lower_shadow(i-1));
        if bear_shadow_body_ratio(i-1) >= 1.5
            middle_bear_body(i-1)=(j_data(i-1,4)+j_data(i-1,1))/2;
            if middle_bear_body(i-1) > j_data(i,2)
                if j_data(i+1,1) > j_data(i+1,4)
                    bull_upper_shadow(i+1)=j_data(i+1,2)-j_data(i+1,1);
                    bull_lower_shadow(i+1)=j_data(i+1,4)-j_data(i+1,3);
                    bull_body_size(i+1)=j_data(i+1,1)-j_data(i+1,4);
                    bull_shadow_body_ratio(i+1) = bull_body_size(i+1)./(bull_upper_shadow(i+1)+bull_lower_shadow(i+1));
                    if bull_shadow_body_ratio(i+1) >= 1.5
                        middle_bear_body(i+1)=(j_data(i+1,1)+j_data(i+-1,4))/2;
                        if middle_bear_body(i+1) > j_data(i,2) && middle_bear_body(i-1) < j_data(i+1,2)
                           disp('DOJI STAR MORNING STAR')
                           i
                           i+1
                           totalDSMS=totalDSMS+1;
                        end
                    end
                end
            end
        end
       elseif j_data(i-1,4) > j_data(i-1,1)
           bull_upper_shadow(i-1)=j_data(i-1,2)-j_data(i-1,4);
           bull_lower_shadow(i-1)=j_data(i-1,1)-j_data(i-1,3);
           bull_body_size(i-1)=j_data(i-1,4)-j_data(i-1,1);
           bull_shadow_body_ratio(i-1) = bull_body_size(i-1)./(bull_upper_shadow(i-1)+bull_lower_shadow(i-1));
           if bull_shadow_body_ratio(i-1) >= 1.5
               bull_body_middle(i-1)=(j_data(i-1,1)+j_data(i-1,4))/2;
               if bull_body_middle(i-1) < j_data(i,3)
                   if j_data(i+1,4) > j_data(i+1,1)
                       bear_upper_shadow(i+1)=j_data(i+1,2)-j_data(i+1,1);
                       bear_lower_shadow(i+1)=j_data(i+1,4)-j_data(i+1,3);
                       bear_body_size(i+1)=j_data(i+1,1)-j_data(i+1,4);
                       bear_shadow_body_ratio(i+1) = bear_body_size(i+1)./(bear_upper_shadow(i+1)+bear_lower_shadow(i+1));
                       if bull_shadow_body_ratio(i+1) >= 1.5
                           bull_body_middle(i+1)=(j_data(i+1,1)+j_data(i+1,4))/2;
                           if bull_body_middle(i+1) < j_data(i,3)
                               disp('DOJI STAR EVENING STAR')
                               i
                               i+1
                               totalDSES=totalDSES+1;
                           end
                       end
                   end
               end
           end
       end
       end
   elseif bodysizes(i) > 0 && bodysizes(i) <= 0.1
       if j_data(i,1) > j_data(i,4)
        bear_upper_shadow(i)=j_data(i,2)-j_data(i,1);
        bear_lower_shadow(i)=j_data(i,4)-j_data(i,3);
        bear_body_size(i)=j_data(i,1)-j_data(i,4);
        bear_body_shadow_ratio(i)=bear_body_size(i)./(bear_lower_shadow(i)+bear_upper_shadow(i));
        if bear_body_shadow_ratio(i) <= 0.1
            bear_shadow_ratio(i)=bear_upper_shadow(i)./bear_lower_shadow(i);
            if bear_shadow_ratio(i) >= 0.8 && bear_shadow_ratio(i) <= 1.2
                disp('BEAR DOJI')
                i
                totalBeDoji=totalBeDoji+1;
                if j_data(i+1,4) > j_data(i+1,1)
                                            bull_upper_shadow(i+1)=j_data(i+1,2)-j_data(i+1,4);
                                            bull_lower_shadow(i+1)=j_data(i+1,1)-j_data(i+1,3);
                                            bull_body_size(i+1)=j_data(i+1,4)-j_data(i+1,1);
                                            bull_shadow_body_ratio(i+1) = bull_body_size(i+1)./(bull_upper_shadow(i+1)+bull_lower_shadow(i+1));
                                            if bull_shadow_body_ratio(i+1) >= 1.25
                                                middle_bull_body(i+1)=(j_data(i+1,4)+j_data(i+1,1))/2;
                                                if middle_bull_body(i+1) > j_data(i,2)
                                                    if j_data(i,4) > middle_bear_body
                                                        disp('BEAR DOJI MORNING STAR')
                                                        i
                                                        i+1
                                                        totalBeDMS=totalBeDMS+1;
                                                    end
                                                end
                                            end
                end
            end
        end
        elseif j_data(i+1,1) > j_data(i+1,4)
                    bear_upper_shadow(i+1)=j_data(i+1,2)-j_data(i+1,1);
                    bear_lower_shadow(i+1)=j_data(i+1,4)-j_data(i+1,3);
                    bear_body_size(i+1)=j_data(i+1,1)-j_data(i+1,4);
                    bear_shadow_body_ratio(i+1) = bear_body_size(i+1)./(bear_upper_shadow(i+1)+bear_lower_shadow(i+1));
                    if bear_shadow_body_ratio(i+1) >= 1.5
                        middle_bear_body(i+1)=(j_data(i+1,1)+j_data(i+1,4))/2;
                        if middle_bear_body(i+1) < j_data(i,3)
                                disp('BEAR DOJI EVENING STAR')
                                i
                                i+1
                                totalBeDES=totalBeDES+1;
                        end
                    end
       elseif j_data(i,4) > j_data(i,1)
        bull_upper_shadow(i)=j_data(i,2)-j_data(i,4);
        bull_lower_shadow(i)=j_data(i,1)-j_data(i,3);
        bull_body_size(i)=j_data(i,4)-j_data(i,1);
        bull_body_shadow_ratio(i)=bull_body_size(i)./(bull_lower_shadow(i)+bull_upper_shadow(i));
        if bull_body_shadow_ratio(i) <= 0.1
            bull_shadow_ratio(i)=bull_upper_shadow(i)./bull_lower_shadow(i);
            if bull_shadow_ratio(i) >= 0.8 && bull_shadow_ratio(i) <= 1.2
                disp('BULL DOJI')
                i
                totalBuDoji=totalBuDoji;
                if j_data(i+1,4) > j_data(i+1,1)
                                bull_upper_shadow(i+1)=j_data(i+1,2)-j_data(i+1,4);
                                bull_lower_shadow(i+1)=j_data(i+1,1)-j_data(i+1,3);
                                bull_body_size(i+1)=j_data(i+1,4)-j_data(i+1,1);
                                bull_shadow_body_ratio(i+1) = bull_body_size(i+1)./(bull_upper_shadow(i+1)+bull_lower_shadow(i+1));
                                if bull_shadow_body_ratio(i+1) >= 1.25
                                    middle_bull_body(i+1)=(j_data(i+1,4)+j_data(i+1,1))/2;
                                    if middle_bull_body(i+1) > j_data(i,2)
                                        if j_data(i+1,4) > middle_bear_body
                                        disp('BULL DOJI MORNING STAR')
                                        i
                                        i+1
                                        totalBuDMS=totalBuDMS+1;
                                        end
                                    end
                                end
                 elseif j_data(i+1,1) > j_data(i+1,4)
                                            bear_upper_shadow(i+1)=j_data(i+1,2)-j_data(i+1,1);
                                            bear_lower_shadow(i+1)=j_data(i+1,4)-j_data(i+1,3);
                                            bear_body_size(i+1)=j_data(i+1,1)-j_data(i+1,4);
                                            bear_shadow_body_ratio(i+1) = bear_body_size(i+1)./(bear_upper_shadow(i+1)+bear_lower_shadow(i+1));
                                            if bear_shadow_body_ratio(i+1) >= 1.5
                                                middle_bear_body(i+1)=(j_data(i+1,1)+j_data(i+1,4))/2;
                                                if middle_bear_body(i+1) < j_data(i,3)
                                                    if j_data(i+1,4) < middle_bull_body(i-1)
                                                        disp('BULL DOJI EVENING STAR')
                                                        i
                                                        i+1
                                                        totalBuDES=totalBuDES+1;
                                                    end
                                                end
                                            end
                end
            end
        end
       end
   end
end
totalDFDoji
totalGSDoji
totalDojiStar
totalDojiSta
totalDES
totalDMS
totalBeST
totalBeHang
totalBeIHang
totalBeDoji
totalBuST
totalBuH
totalBuIH
totalBuDoji
totalBuMaru
totalBeMaru
totalBuDES
totalBeDES
totalBuDMS
totalBeDMS
totalDSES
totalDSMS
