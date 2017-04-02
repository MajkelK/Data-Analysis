# -*- coding: utf-8 -*-
"""
Created on 23-Mar-2017 by Michal Konieczny


"""
import pandas as pd
import numpy as np


data = pd.read_csv('nesarc_pds.csv', low_memory = False)

#print(len(data))
#print(len(data.columns))

print("Distribution of variables relating to depression resulting in unusual activity")

print("Distribution of: HAD TROUBLE FALLING ASLEEP NEARLY EVERY DAY FOR 2+ WEEKS")
print("1 - Yes, 2 - No, 9, Unknown")
data1 = data[(data["S4AQ4A5"] != " ")]
v1_counts = data1["S4AQ4A5"].value_counts(sort=False)
v1_perc = data1["S4AQ4A5"].value_counts(sort=False, normalize = True)
print(v1_counts)
print(sum(v1_counts))
print(v1_perc)


print("Distribution of: WOKE UP TOO EARLY NEARLY EVERY DAY FOR 2+ WEEKS")
print("1 - Yes, 2 - No, 9, Unknown")
data2 = data[(data["S4AQ4A6"] != " ")]
v2_counts = data2["S4AQ4A6"].value_counts(sort=False)
v2_perc = data2["S4AQ4A6"].value_counts(sort=False, normalize = True)
print(v2_counts)
print(sum(v2_counts))
print(v2_perc)


print("Distribution of: FIDGETED/PACED MOST OF THE TIME FOR 2+ WEEKS")
print("1 - Yes, 2 - No, 9, Unknown")
data3 = data[(data["S4AQ4A10"] != " ")]
v3_counts = data3["S4AQ4A10"].value_counts(sort=False)
v3_perc = data3["S4AQ4A10"].value_counts(sort=False, normalize = True)
print(v3_counts)
print(sum(v3_counts))
print(v3_perc)


print("Distribution of: BECAME SO RESTLESS THAT FELT UNCOMFORTABLE FOR 2+ WEEKS")
print("1 - Yes, 2 - No, 9, Unknown")
data4 = data[(data["S4AQ4A11"] != " ")]
v4_counts = data4["S4AQ4A11"].value_counts(sort=False)
v4_perc = data4["S4AQ4A11"].value_counts(sort=False, normalize = True)
print(v4_counts)
print(sum(v4_counts))
print(v4_perc)
