import sys
sys.path.append('../tools')

import getanalysis
import tradesim
import csv
import time
import numpy
import pylab

jdata_filepath = '../../data/jcandles.csv'
hadata_filepath = '../../data/hacandles.csv'
jdata = getanalysis.import_j_candles(jdata_filepath)
hadata = getanalysis.import_j_candles(hadata_filepath)

[jincrease_data, jbody_sizes, jshadow_sizes, data_length] = getanalysis.body_and_shadow(jdata)
[jrun_length_data, jreversals] = getanalysis.runs_and_reversal(jdata, data_length, jincrease_data)

[haincrease_data, habody_sizes, hashadow_sizes, data_length] = getanalysis.body_and_shadow(hadata)
[harun_length_data, hareversals] = getanalysis.runs_and_reversal(hadata, data_length, haincrease_data)

jrun_function_data = getanalysis.run_analysis(jbody_sizes, data_length, jrun_length_data, jincrease_data)
harun_function_data = getanalysis.run_analysis(habody_sizes, data_length, harun_length_data, haincrease_data)

coefficient_data = []

# Japanese candle data first
for i in range(data_length):
    if jreversals[i] == 1 and jincrease_data[i] == 1:
        # Reversal at start of climb
        this_climb_profit = jrun_function_data[i][4]
        this_climb_length = jrun_function_data[i][3]
        this_body_size = jbody_sizes[i]
        this_shadow_size = jshadow_sizes[i]
        try:
            this_body_shadow_ratio = this_body_size / this_shadow_size
        except:
            this_body_shadow_ratio = 1
        this_imm_prev_body_size = jbody_sizes[i-1]
        this_imm_prev_shadow_size = jshadow_sizes[i-1]
        try:
            this_imm_prev_body_shadow_ratio = this_imm_prev_body_size / this_imm_prev_shadow_size
        except:
            this_imm_prev_body_shadow_ratio = 1
        this_prev_run_length = jrun_function_data[i][1]
        this_prev_run_diff = jrun_function_data[i][2]
        prev_body_sizes = []
        prev_shadow_sizes = []
        prev_body_shadow_ratios = []
        for j in range(this_prev_run_length):
            prev_body_sizes.append(jbody_sizes[i-(j+1)])
            prev_shadow_sizes.append(jshadow_sizes[i-(j+1)])
            try:
                prev_body_shadow_ratios.append((jbody_sizes[i-(j+1)]/jshadow_sizes[i-(j+1)]))
            except:
                prev_body_shadow_ratios.append(1)
        this_prev_av_body_size = numpy.mean(prev_body_sizes)
        this_prev_av_shadow_size = numpy.mean(prev_shadow_sizes)
        this_prev_av_body_shadow_ratio = numpy.mean(prev_body_shadow_ratios)
        coefficient_data.append([i, this_climb_profit, this_climb_length, this_body_size, this_shadow_size,
                                 this_body_shadow_ratio, this_imm_prev_body_size, this_imm_prev_shadow_size,
                                 this_imm_prev_body_shadow_ratio, this_prev_run_length, this_prev_run_diff,
                                 this_prev_av_body_size, this_prev_av_shadow_size,
                                 this_prev_av_body_shadow_ratio])
        
# Heikin Ashi candle data after
hacoefficient_data = []
for i in range(data_length):
    if hareversals[i] == 1 and haincrease_data[i] == 1:
        # Reversal at start of climb
        this_climb_profit = harun_function_data[i][4]
        this_climb_length = harun_function_data[i][3]
        this_body_size = habody_sizes[i]
        this_shadow_size = hashadow_sizes[i]
        try:
            this_body_shadow_ratio = this_body_size / this_shadow_size
        except:
            this_body_shadow_ratio = 1
        this_imm_prev_body_size = habody_sizes[i-1]
        this_imm_prev_shadow_size = hashadow_sizes[i-1]
        try:
            this_imm_prev_body_shadow_ratio = this_imm_prev_body_size / this_imm_prev_shadow_size
        except:
            this_imm_prev_body_shadow_ratio = 1
        this_prev_run_length = harun_function_data[i][1]
        this_prev_run_diff = harun_function_data[i][2]
        prev_body_sizes = []
        prev_shadow_sizes = []
        prev_body_shadow_ratios = []
        for j in range(this_prev_run_length):
            prev_body_sizes.append(habody_sizes[i-(j+1)])
            prev_shadow_sizes.append(hashadow_sizes[i-(j+1)])
            try:
                prev_body_shadow_ratios.append((habody_sizes[i-(j+1)]/hashadow_sizes[i-(j+1)]))
            except:
                prev_body_shadow_ratios.append(1)
        this_prev_av_body_size = numpy.mean(prev_body_sizes)
        this_prev_av_shadow_size = numpy.mean(prev_shadow_sizes)
        this_prev_av_body_shadow_ratio = numpy.mean(prev_body_shadow_ratios)
        hacoefficient_data.append([i, this_climb_profit, this_climb_length, this_body_size, this_shadow_size,
                                 this_body_shadow_ratio, this_imm_prev_body_size, this_imm_prev_shadow_size,
                                 this_imm_prev_body_shadow_ratio, this_prev_run_length, this_prev_run_diff,
                                 this_prev_av_body_size, this_prev_av_shadow_size,
                                 this_prev_av_body_shadow_ratio])
        
'''
# Save Japanese candle coefficient data to csv
with open('../data/analysis/coefficientanalysis.csv', 'wb') as file:
    writer = csv.writer(file, delimiter=',')
    for data_line in coefficient_data:
        writer.writerow(data_line)
'''

# Save Heikin Ashi candle coefficient data to csv
with open('../../data/analysis/hacoefficientanalysis.csv', 'wb') as file:
    writer = csv.writer(file, delimiter=',')
    for data_line in hacoefficient_data:
        writer.writerow(data_line)

'''
# Save all Japanese candle graphs
filepath = '../data/analysis/graphs/'
graph_titles = (['body_sizes', 'shadow_sizes', 'body_to_shadow_ratio', 'prev_body_size', 'prev_shadow_size',
                'prev_body_shadow_ratio', 'prev_run_length', 'prev_run_diff', 'prev_av_body_size',
                'prev_av_shadow_size', 'prev_av_body_shadow_ratio'])

plot_arr = numpy.array([[0.0]*len(coefficient_data)]*(len(graph_titles)+1))
for i in range(len(coefficient_data)):
    plot_arr[0][i] = coefficient_data[i][1]
    for j in range(len(graph_titles)):
        plot_arr[j+1][i] = coefficient_data[i][j+3]
    
for i in range(len(graph_titles)):
    this_graph_title = graph_titles[i]
    this_filepath = filepath + this_graph_title + '.png'
    pylab.cla()
    pylab.scatter(plot_arr[i+1], plot_arr[0])
    pylab.xlabel(this_graph_title)
    pylab.ylabel('profit')
    pylab.savefig(this_filepath)
'''

# Save all Heikin Ashi candle graphs
filepath = '../../data/analysis/hagraphs/'
graph_titles = (['body_sizes', 'shadow_sizes', 'body_to_shadow_ratio', 'prev_body_size', 'prev_shadow_size',
                'prev_body_shadow_ratio', 'prev_run_length', 'prev_run_diff', 'prev_av_body_size',
                'prev_av_shadow_size', 'prev_av_body_shadow_ratio'])

plot_arr = numpy.array([[0.0]*len(hacoefficient_data)]*(len(graph_titles)+1))
for i in range(len(hacoefficient_data)):
    plot_arr[0][i] = hacoefficient_data[i][1]
    for j in range(len(graph_titles)):
        plot_arr[j+1][i] = hacoefficient_data[i][j+3]
    
for i in range(len(graph_titles)):
    this_graph_title = graph_titles[i]
    this_filepath = filepath + this_graph_title + '.png'
    pylab.cla()
    pylab.scatter(plot_arr[i+1], plot_arr[0])
    pylab.xlabel(this_graph_title)
    pylab.ylabel('profit')
    pylab.savefig(this_filepath)
