# -*- coding: utf-8 -*-
"""
Created on Sun May  7 12:51:53 2017

@author: Michał
"""

import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
import statsmodels.stats.multicomp as multi 

data = pd.read_csv('nesarc_pds.csv', low_memory = False)

#setting variables to numeric
data['S2AQ8A'] = data['S2AQ8A'].convert_objects(convert_numeric = True)
data['S1Q9B'] = data['S1Q9B'].convert_objects(convert_numeric = True)
data['S2AQ8B'] = data['S2AQ8B'].convert_objects(convert_numeric = True)
data['SEX'] = data['SEX'].convert_objects(convert_numeric = True)

#replace 99 with NaN
data['S2AQ8A']=data['S2AQ8A'].replace(99, np.nan)
data['S2AQ8B']=data['S2AQ8B'].replace(99, np.nan)

#recoding number of days drinking in a year
recode1 = {1: 365, 2: 340, 3: 182, 4: 104, 5: 52, 6: 30, 7: 12, 8: 9, 9: 4.5, 10: 1.5}
data['ALC_YEAR'] = data['S2AQ8A'].map(recode1)

data['ALC_YEAR'] = data['ALC_YEAR'].convert_objects(convert_numeric = True)

#multiply by number of drinks in a day
data['ALC_DRINK_YR'] = data['ALC_YEAR'] * data['S2AQ8B']


# Use OLS to examine relationship between number of drinks and major depression
model1 = smf.ols(formula='ALC_DRINK_YR ~ C(MAJORDEPLIFE)', data=data)
results1 = model1.fit()
print (results1.summary())

#run means by depression status

sub = data[['ALC_DRINK_YR', 'MAJORDEPLIFE']].dropna()

print ('means for ALC_DRINK_YR by major depression status')
means1= sub.groupby('MAJORDEPLIFE').mean()
print (means1)

print ('standard deviations for ALC_DRINK_YR by major depression status')
sd1 = sub.groupby('MAJORDEPLIFE').std()
print (sd1)

#Examine the relationship again adding a moderator variable - gender
sub_male = data[(data['SEX'] == 1)]
sub_female = data[(data['SEX'] == 2)]

# run ANOVA for male subset
male= sub_male[['ALC_DRINK_YR', 'MAJORDEPLIFE']].dropna()
model_male = smf.ols(formula='ALC_DRINK_YR ~ C(MAJORDEPLIFE)', data=male)
results_male = model_male.fit()
print('Association between depression and number of alcoholic drinks for males')
print (results_male.summary())

# run means and standard deviation for male subset
print ('means for ALC_DRINK_YR by major depression status')
means_m= male.groupby('MAJORDEPLIFE').mean()
print (means_m)

print ('standard deviations for ALC_DRINK_YR by major depression status')
sd_m = male.groupby('MAJORDEPLIFE').std()
print (sd_m)

# run ANOVA for female subset
female= sub_female[['ALC_DRINK_YR', 'MAJORDEPLIFE']].dropna()
model_female = smf.ols(formula='ALC_DRINK_YR ~ C(MAJORDEPLIFE)', data=female)
results_female = model_female.fit()
print('Association between depression and number of alcoholic drinks for females')
print (results_female.summary())

# run means and standard deviation for female subset
print ('means for ALC_DRINK_YR by major depression status')
means_f= female.groupby('MAJORDEPLIFE').mean()
print (means_f)

print ('standard deviations for ALC_DRINK_YR by major depression status')
sd_f = female.groupby('MAJORDEPLIFE').std()
print (sd_f)

# examine number of drinks split by occupation

sub2 = data[['ALC_YEAR', 'S1Q9B']].dropna()

model2 = smf.ols(formula='ALC_YEAR ~ C(S1Q9B)', data=sub2).fit()
print (model2.summary())

print ('means for ALC_YEAR by major depression status')
means2= sub2.groupby('S1Q9B').mean()
print (means2)

print ('standard deviations for ALC_YEAR by major depression status')
sd2 = sub2.groupby('S1Q9B').std()
print (sd2)

# post hoc test

mc1 = multi.MultiComparison(sub2['ALC_YEAR'], sub2['S1Q9B'])
res1 = mc1.tukeyhsd()
print(res1.summary())





