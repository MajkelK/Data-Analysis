# -*- coding: utf-8 -*-
"""
Created on Sun May 21 20:23:14 2017

@author: Michał
"""

import pandas as pd
import numpy as np
import seaborn
import scipy
import matplotlib.pyplot as plt

data = pd.read_csv('nesarc_pds.csv', low_memory = False)

#Number of episodes of depression

data['S4AQ7'] = data['S4AQ7'].convert_objects(convert_numeric = True)
# Replace missing and unknowwn values with blanks
data["S4AQ7"] = data["S4AQ7"].replace([" ",99], np.NaN)


#Number of episodes of pathological gambling

data['S12Q3E'] = data['S12Q3E'].convert_objects(convert_numeric = True)
# Replace missing and unknowwn values with blanks
data["S12Q3E"] = data["S12Q3E"].replace([" ",99], np.NaN)

data_cl = data.dropna()

#generate scatterplot
scat = seaborn.regplot(x="S4AQ7", y="S12Q3E", fit_reg=True, data=data_cl)
plt.xlabel('No. of depression episodes')
plt.ylabel('No. of gambling episodes')
plt.title('Scatterplot for the Association between depression and gambling')

#generate Pearson coefficient
print ('association between depression and gambling')
print (scipy.stats.pearsonr(data_cl['S4AQ7'], data_cl['S12Q3E']))
