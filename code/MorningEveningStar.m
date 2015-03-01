totalBuDES=0;
totalBeDES=0;
totalBuDMS=0;
totalBeDMS=0;
for i = 1:5000
   if bodysizes(i) == 0
       upper_shadow(i)=j_data(i,2)-j_data(i,1);
       lower_shadow(i)=j_data(i,4)-j_data(i,3);
       shadow_ratio(i)=upper_shadow(i)./lower_shadow(i);
       if shadow_ratio(i) >= 0.8 && shadow_ratio(i) <= 1.2
       disp('DOJI STAR')
       i
       totalDoji=totalDoji+1;
       if j_data(i-1,1) > j_data(i-1,4)
        bear_upper_shadow(i-1)=j_data(i-1,2)-j_data(i-1,1);
        bear_lower_shadow(i-1)=j_data(i-1,4)-j_data(i-1,3);
        bear_body_size(i-1)=j_data(i-1,1)-j_data(i-1,4);
        bear_shadow_body_ratio(i-1) = bear_body_size(i-1)./(bear_upper_shadow(i-1)+bear_lower_shadow(i-1));
        if bear_shadow_body_ratio(i-1) >= 1.5
            middle_bear_body(i-1)=(j_data(i-1,1)+j_data(i-1,4))/2;
            if middle_bear_body(i-1) > j_data(i,2)
                disp('DOJI STAR MORNING STAR')
                i
                totalDSMS=totalDSMS+1;
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
                   disp('DOJI STAR EVENING STAR')
                   i
                   totalDSES=totalDSES+1;
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
                if j_data(i-1,4) < j_data(i-1,1)
                    bear_upper_shadow(i-1)=j_data(i-1,2)-j_data(i-1,1);
                    bear_lower_shadow(i-1)=j_data(i-1,4)-j_data(i-1,3);
                    bear_body_size(i-1)=j_data(i-1,1)-j_data(i-1,4);
                    bear_shadow_body_ratio(i-1) = bear_body_size(i-1)./(bear_upper_shadow(i-1)+bear_lower_shadow(i-1));
                    if bear_shadow_body_ratio(i-1) >= 1.5
                        middle_bear_body(i-1)=(j_data(i-1,1)+j_data(i-1,4))/2;
                        if middle_bear_body(i-1) > j_data(i,2)
                            if j_data(i+1,4) > j_data(i+1,1)
                                bull_upper_shadow(i+1)=j_data(i+1,2)-j_data(i+1,4);
                                bull_lower_shadow(i+1)=j_data(i+1,1)-j_data(i+1,3);
                                bull_body_size(i+1)=j_data(i+1,4)-j_data(i+1,1);
                                bull_shadow_body_ratio(i+1) = bull_body_size(i+1)./(bull_upper_shadow(i+1)+bull_lower_shadow(i+1));
                                if bull_shadow_body_ratio(i+1) >= 1.25
                                    middle_bull_body(i+1)=(j_data(i+1,4)+j_data(i+1,1))/2;
                                    if middle_bull_body(i+1) > j_data(i,2)
                                        if j_data(i+1,4) > middle_bear_body
                                        disp('BEAR DOJI MORNING STAR')
                                        i
                                        totalBeDMS=totalBeDMS+1;
                                        end
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
                                if bull_shadow_body_ratio(i-1) >= 1.25
                                    middle_bull_body(i-1)=(j_data(i-1,4)+j_data(i-1,1))/2;
                                    if middle_bull_body(i-1) < j_data(i,3)
                                        if j_data(i+1,1) > j_data(i+1,4)
                                            bear_upper_shadow(i+1)=j_data(i+1,2)-j_data(i+1,1);
                                            bear_lower_shadow(i+1)=j_data(i+1,4)-j_data(i+1,3);
                                            bear_body_size(i+1)=j_data(i+1,1)-j_data(i+1,4);
                                            bear_shadow_body_ratio(i+1) = bear_body_size(i+1)./(bear_upper_shadow(i+1)+bear_lower_shadow(i+1));
                                            if bear_shadow_body_ratio(i+1) >= 1.5
                                                middle_bear_body(i+1)=(j_data(i+1,1)+j_data(i+1,4))/2;
                                                if middle_bear_body(i+1) < j_data(i,3)
                                                    if j_data(i+1,4) < middle_bull_body(i-1)
                                                        disp('BEAR DOJI EVENING STAR')
                                                        i
                                                        totalBeDES=totalBeDES+1;
                                                    end
                                                end
                                            end
                                        end
                                    end
                                end
                end
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
                totalBuDoji=BuDoji;
                if j_data(i-1,1) > j_data(i-1,4)
                    bear_upper_shadow(i-1)=j_data(i-1,2)-j_data(i-1,1);
                    bear_lower_shadow(i-1)=j_data(i-1,4)-j_data(i-1,3);
                    bear_body_size(i-1)=j_data(i-1,1)-j_data(i-1,4);
                    bear_shadow_body_ratio(i-1) = bear_body_size(i-1)./(bear_upper_shadow(i-1)+bear_lower_shadow(i-1));
                    if bear_shadow_body_ratio(i-1) >= 1.5
                        middle_bear_body(i-1)=(j_data(i-1,1)+j_data(i-1,4))/2;
                        if middle_bear_body(i-1) > j_data(i,2)
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
                                        totalBuDMS=totalBuDMS+1;
                                        end
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
                                if bull_shadow_body_ratio(i-1) >= 1.25
                                    middle_bull_body(i-1)=(j_data(i-1,4)+j_data(i-1,1))/2;
                                    if middle_bull_body(i-1) < j_data(i,3)
                                        if j_data(i+1,1) > j_data(i+1,4)
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
       end
   end
end
totalDFDoji
totalGSDoji
totalDojiStar
totalDoji
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