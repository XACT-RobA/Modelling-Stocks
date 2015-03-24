import sys
sys.path.append('./tools')

import getanalysis
import tradesim
import csv
import time
import numpy

# Import Japanese data
jdata_filepath = '../data/jcandles.csv'
jdata = getanalysis.import_j_candles(jdata_filepath)
[jincrease_data, jbody_sizes, jshadow_sizes, data_length] = getanalysis.body_and_shadow(jdata)
[jrun_length_data, jreversals] = getanalysis.runs_and_reversal(jdata, data_length, jincrease_data)
jrun_function_data = getanalysis.run_analysis(jbody_sizes, data_length, jrun_length_data, jincrease_data)

# Import Heikin Ashi data
hadata_filepath = '../data/hacandles.csv'
hadata = getanalysis.import_j_candles(hadata_filepath)
[haincrease_data, habody_sizes, hashadow_sizes, data_length] = getanalysis.body_and_shadow(hadata)
[harun_length_data, hareversals] = getanalysis.runs_and_reversal(hadata, data_length, haincrease_data)
harun_function_data = getanalysis.run_analysis(habody_sizes, data_length, harun_length_data, haincrease_data)

def calculateprofit():
    return 0

# Code will iterate through each factor using either percentiles or values
# defined by values set in a controlling array
# Factors included are:
# Reversal - Body size, Shadow size, Body to shadow ratio
# Candle before reversal - Body size, Shadow size, Body to shadow ratio
# Run before reversal - Run length, Difference of values
# Candles in run before reversal - Average body size, Average shadow size
# Average body to shadow ratio

