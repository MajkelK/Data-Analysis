# -*- coding: utf-8 -*-
"""
Created on Sun May  7 12:51:53 2017

@author: Michał
"""

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi 
import statsmodels.api as sm
import seaborn
import matplotlib.pyplot as plt

data = pd.read_csv('nesarc_pds.csv', low_memory = False)

#########################
# Data management


#setting variables to numeric
data['S2AQ8A'] = data['S2AQ8A'].convert_objects(convert_numeric = True)
data['S1Q9B'] = data['S1Q9B'].convert_objects(convert_numeric = True)
data['S2AQ8B'] = data['S2AQ8B'].convert_objects(convert_numeric = True)
data['SEX'] = data['SEX'].convert_objects(convert_numeric = True)
data['DAYS_HOSP'] = data['S13Q2'].convert_objects(convert_numeric = True) #days stayed in hospital
data['CRIME_VICT'] = data['S13Q5'].convert_objects(convert_numeric = True) #number of times victim of a crime
data['AGE_MARR'] = data['S1Q4A'].convert_objects(convert_numeric = True) #age at first marriage
data['ETHANOL_CONS'] = data['ETOTLCA2'].convert_objects(convert_numeric = True) #AVERAGE DAILY VOLUME OF ETHANOL CONSUMED IN PAST YEAR


#replace 99 with NaN
data['S2AQ8A']=data['S2AQ8A'].replace(99, np.nan)
data['S2AQ8B']=data['S2AQ8B'].replace(99, np.nan)
data['DAYS_HOSP']=data['DAYS_HOSP'].replace(999, np.nan)
data['CRIME_VICT']=data['CRIME_VICT'].replace(99, np.nan)
data['AGE_MARR']=data['AGE_MARR'].replace(99, np.nan)
data['SEX']=data['SEX'].replace(2, 0) # recode so female is coded as 0
data['ETHANOL_CONS']=data['ETHANOL_CONS']*28.3 #recode to grams

# remove outliers (does not work)

def var1 (row):
   if row['ETHANOL_CONS'] > 1000 :
      return np.nan
   else :
       return row['ETHANOL_CONS']
   data['ETHANOL_CONS'] = data.apply (lambda row: var1 (row),axis=1)

#recoding number of days drinking in a year
recode1 = {1: 365, 2: 340, 3: 182, 4: 104, 5: 52, 6: 30, 7: 12, 8: 9, 9: 4.5, 10: 1.5}
data['ALC_YEAR'] = data['S2AQ8A'].map(recode1)

data['ALC_YEAR'] = data['ALC_YEAR'].convert_objects(convert_numeric = True)

#multiply by number of drinks in a day
data['ALC_DRINK_YR'] = data['ALC_YEAR'] * data['S2AQ8B']

sub = data[['ETHANOL_CONS', 'ALC_DRINK_YR', 'MAJORDEPLIFE', 'SEX', 'DAYS_HOSP', 'CRIME_VICT', 'AGE_MARR']].dropna()

print (sub.count())

#########################

# Center the explanatory variables:

sub['DAYS_HOSP_C'] = sub['DAYS_HOSP'] - sub['DAYS_HOSP'].mean()
sub['CRIME_VICT_C'] = sub['CRIME_VICT'] - sub['CRIME_VICT'].mean()
sub['AGE_MARR_C'] = sub['AGE_MARR'] - sub['AGE_MARR'].mean()

# check the mean

print(sub['DAYS_HOSP_C'].mean())
print(sub['CRIME_VICT_C'].mean())
print(sub['AGE_MARR_C'].mean())

# generate scatterplots for relation between explanatory and response variables

scat1 = seaborn.regplot(y="ETHANOL_CONS", x="DAYS_HOSP", scatter=True, data=sub)
plt.ylabel('Average grams of ethanol consumed daily')
plt.xlabel('Days spent in hospital in last 12 months')

scat2 = seaborn.regplot(y="ETHANOL_CONS", x="CRIME_VICT", scatter=True, data=sub)
plt.ylabel('Average grams of ethanol consumed daily')
plt.xlabel('Number of times victim of a crime in last 12 months')

scat3 = seaborn.regplot(y="ETHANOL_CONS", x="AGE_MARR", scatter=True, data=sub)
plt.ylabel('Average grams of ethanol consumed daily')
plt.xlabel('Age when first married')

# model multiple regression

model1 = smf.ols('ETHANOL_CONS ~ DAYS_HOSP_C + CRIME_VICT_C + AGE_MARR_C', data=sub).fit()
print(model1.summary())

# qq plot

chart1 = sm.qqplot(model1.resid, line = 'r')


# simple plot of residuals
chart2 =pd.DataFrame(model1.resid_pearson)
plt.plot(chart2, 'o', ls='None')
l = plt.axhline(y=0, color='r')
plt.ylabel('Standardized Residual')
plt.xlabel('Observation Number')

# leverage plot
chart3=sm.graphics.influence_plot(model1, size=8)
print(chart3)