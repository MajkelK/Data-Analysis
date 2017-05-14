# -*- coding: utf-8 -*-
"""
Created on Sun May 14 18:35:57 2017

@author: Michał
"""

import pandas as pd
import numpy as np
import scipy.stats as scs

data = pd.read_csv('nesarc_pds.csv', low_memory = False)

# Replace missing and unknowwn values with blanks
data["S4AQ4A5"] = data["S4AQ4A5"].replace([" ",9], np.NaN)
data["S4AQ4A6"] = data["S4AQ4A6"].replace([" ",9], np.NaN)
data["S4AQ4A10"] = data["S4AQ4A10"].replace([" ",9], np.NaN)
data["S4AQ4A11"] = data["S4AQ4A11"].replace([" ",9], np.NaN)
data["S12Q2A1"] = data["S12Q2A1"].replace([" ",9], np.NaN)
data["S12Q2A2"] = data["S12Q2A2"].replace([" ",9], np.NaN)

# Convert values to numeric

data["S4AQ4A5"] = data["S4AQ4A5"].convert_objects(convert_numeric = True)
data["S4AQ4A6"] = data["S4AQ4A6"].convert_objects(convert_numeric = True)
data["S4AQ4A10"] = data["S4AQ4A10"].convert_objects(convert_numeric = True)
data["S4AQ4A11"] = data["S4AQ4A11"].convert_objects(convert_numeric = True)
data["S12Q2A1"] = data["S12Q2A1"].convert_objects(convert_numeric = True)
data["S12Q2A2"] = data["S12Q2A2"].convert_objects(convert_numeric = True)

# recode for yes = 1 No = 0

recode = {1:1,2:0}
data["S4AQ4A5"] = data["S4AQ4A5"].map(recode)
data["S4AQ4A6"] = data["S4AQ4A6"].map(recode)
data["S4AQ4A10"] = data["S4AQ4A10"].map(recode)
data["S4AQ4A11"] = data["S4AQ4A11"].map(recode)
data["S12Q2A1"] = data["S12Q2A1"].map(recode)
data["S12Q2A2"] = data["S12Q2A2"].map(recode)

# run chi-square analysis for each pair of variables (4 related to depression
# and 2 related to gambling, 8 analyses in total) to see if they're related.

print("PAIR 1: trouble falling asleep vs gambling to get out of bad mood")                                                     
                                                      
# contingency table of observed counts
ct1=pd.crosstab(data['S4AQ4A5'], data['S12Q2A1'])
print (ct1)

# column percentages
colsum1=ct1.sum(axis=0)
colpct1=ct1/colsum1
print(colpct1)

# chi-square
print ('chi-square value, p value, expected counts')
cs1= scs.chi2_contingency(ct1)
print (cs1)                                                     

print("PAIR 2: waking up early vs gambling to get out of bad mood")                                                      
                                                      
# contingency table of observed counts
ct2=pd.crosstab(data['S4AQ4A6'], data['S12Q2A1'])
print (ct2)

# column percentages
colsum2=ct2.sum(axis=0)
colpct2=ct2/colsum2
print(colpct2)

# chi-square
print ('chi-square value, p value, expected counts')
cs2= scs.chi2_contingency(ct2)
print (cs2)  

print("PAIR 3: fidgeting/pacing vs gambling to get out of bad mood")                                                      
                                                      
# contingency table of observed counts
ct3=pd.crosstab(data['S4AQ4A10'], data['S12Q2A1'])
print (ct3)

# column percentages
colsum3=ct3.sum(axis=0)
colpct3=ct3/colsum3
print(colpct3)

# chi-square
print ('chi-square value, p value, expected counts')
cs3= scs.chi2_contingency(ct3)
print (cs3)  

print("PAIR 4: feeling restless vs gambling to get out of bad mood")                                                      
                                                      
# contingency table of observed counts
ct4=pd.crosstab(data['S4AQ4A11'], data['S12Q2A1'])
print (ct4)

# column percentages
colsum4=ct4.sum(axis=0)
colpct4=ct4/colsum4
print(colpct4)

# chi-square
print ('chi-square value, p value, expected counts')
cs4= scs.chi2_contingency(ct4)
print (cs4) 

print("PAIR 5: trouble falling asleep vs gambling to forget troubles")                                                      
                                                      
# contingency table of observed counts
ct5=pd.crosstab(data['S4AQ4A5'], data['S12Q2A2'])
print (ct5)

# column percentages
colsum5=ct5.sum(axis=0)
colpct5=ct5/colsum5
print(colpct5)

# chi-square
print ('chi-square value, p value, expected counts')
cs5= scs.chi2_contingency(ct5)
print (cs5) 

print("PAIR 6: waking up early vs gambling to forget troubles")                                                      
                                                      
# contingency table of observed counts
ct6=pd.crosstab(data['S4AQ4A6'], data['S12Q2A2'])
print (ct6)

# column percentages
colsum6=ct6.sum(axis=0)
colpct6=ct6/colsum6
print(colpct6)

# chi-square
print ('chi-square value, p value, expected counts')
cs6= scs.chi2_contingency(ct6)
print (cs6) 

print("PAIR 7: fidgeting/pacing vs gambling to forget troubles")                                                      
                                                      
# contingency table of observed counts
ct7=pd.crosstab(data['S4AQ4A10'], data['S12Q2A2'])
print (ct7)

# column percentages
colsum7=ct7.sum(axis=0)
colpct7=ct7/colsum7
print(colpct7)

# chi-square
print ('chi-square value, p value, expected counts')
cs7= scs.chi2_contingency(ct7)
print (cs7) 

print("PAIR 8: feeling restless vs gambling to forget troubles")                                                      
                                                      
# contingency table of observed counts
ct8=pd.crosstab(data['S4AQ4A11'], data['S12Q2A2'])
print (ct8)

# column percentages
colsum8=ct8.sum(axis=0)
colpct8=ct8/colsum8
print(colpct8)

# chi-square
print ('chi-square value, p value, expected counts')
cs8= scs.chi2_contingency(ct8)
print (cs8) 