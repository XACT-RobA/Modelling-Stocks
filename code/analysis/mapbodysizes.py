import sys
sys.path.append('../tools')

import getanalysis
import tradesim

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

filepath = '../../data/jcandles.csv'

data = getanalysis.import_j_candles(filepath)

[increase_data, body_sizes, shadow_sizes, data_length] = getanalysis.body_and_shadow(data)

#tradesim.save_trade_array(body_sizes, '../../data/bodysizes.csv')


h = sorted(body_sizes)  #sorted
hmean = np.mean(h)
hstd = np.std(h)
pdf = stats.norm.pdf(h, hmean, hstd)
plt.plot(h, pdf)
for i in range(5):
	plt.plot([np.percentile(body_sizes, (25*i)), np.percentile(body_sizes, (25*i))], [0,600], 'r--')
plt.xlabel('Body size')
plt.ylabel('Frequency')
plt.title('Frequency distribution of body sizes, with quartiles')
plt.show()
