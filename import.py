# -*- coding: utf-8 -*-
"""
Created on 23-Mar-2017 by Michal Konieczny

"""
import pandas as pd
import numpy as np
import seaborn
import matplotlib.pyplot as plt


data = pd.read_csv('nesarc_pds.csv', low_memory = False)

#print(len(data))
#print(len(data.columns))

# Save a copy of the original dataset
data_copy = data.copy()

# Replace missing and unknowwn values with blanks
data["S4AQ4A5"] = data["S4AQ4A5"].replace([" ",9], np.NaN)
data["S4AQ4A6"] = data["S4AQ4A6"].replace([" ",9], np.NaN)
data["S4AQ4A10"] = data["S4AQ4A10"].replace([" ",9], np.NaN)
data["S4AQ4A11"] = data["S4AQ4A11"].replace([" ",9], np.NaN)

# Convert values to numeric

data["S4AQ4A5"] = data["S4AQ4A5"].convert_objects(convert_numeric = True)
data["S4AQ4A6"] = data["S4AQ4A6"].convert_objects(convert_numeric = True)
data["S4AQ4A10"] = data["S4AQ4A10"].convert_objects(convert_numeric = True)
data["S4AQ4A11"] = data["S4AQ4A11"].convert_objects(convert_numeric = True)

# Code 'No' answers as 0 to facilitate later calculations

recode = {1:1,2:0}
data["S4AQ4A5"] = data["S4AQ4A5"].map(recode)
data["S4AQ4A6"] = data["S4AQ4A6"].map(recode)
data["S4AQ4A10"] = data["S4AQ4A10"].map(recode)
data["S4AQ4A11"] = data["S4AQ4A11"].map(recode)

print("Distribution of variables relating to depression resulting in unusual activity")

print("Distribution of: HAD TROUBLE FALLING ASLEEP NEARLY EVERY DAY FOR 2+ WEEKS")
print("1 - Yes, 0 - No")
v1_counts = data["S4AQ4A5"].value_counts(sort=False)
v1_perc = data["S4AQ4A5"].value_counts(sort=False, normalize = True)
print(v1_counts)
print(sum(v1_counts))
print(v1_perc)


print("Distribution of: WOKE UP TOO EARLY NEARLY EVERY DAY FOR 2+ WEEKS")
print("1 - Yes, 0 - No")
v2_counts = data["S4AQ4A6"].value_counts(sort=False)
v2_perc = data["S4AQ4A6"].value_counts(sort=False, normalize = True)
print(v2_counts)
print(sum(v2_counts))
print(v2_perc)

# Create new variable Sleep_Issues that combines troubles falling asleep and waking up early

data["Sleep_issues_num"] = data["S4AQ4A5"] + data["S4AQ4A6"]

print("Distrubution of observations where either or both of above sleep disorders were noted")
print("2 - Both, 1 - One of the two, 0 - None/Unknown")
v2_1_counts = data["Sleep_issues_num"].value_counts(sort=False)
v2_1_perc = data["Sleep_issues_num"].value_counts(sort=False, normalize = True)
print(v2_1_counts)
print(sum(v2_1_counts))
print(v2_1_perc)
    

print("Distribution of: FIDGETED/PACED MOST OF THE TIME FOR 2+ WEEKS")
print("1 - Yes, 0 - No")
v3_counts = data["S4AQ4A10"].value_counts(sort=False)
v3_perc = data["S4AQ4A10"].value_counts(sort=False, normalize = True)
print(v3_counts)
print(sum(v3_counts))
print(v3_perc)


print("Distribution of: BECAME SO RESTLESS THAT FELT UNCOMFORTABLE FOR 2+ WEEKS")
print("1 - Yes, 0 - No")
v4_counts = data["S4AQ4A11"].value_counts(sort=False)
v4_perc = data["S4AQ4A11"].value_counts(sort=False, normalize = True)
print(v4_counts)
print(sum(v4_counts))
print(v4_perc)

# Create new variable Restlessness that combines fidgeting and restlessness

data["Restless_num"] = data["S4AQ4A10"] + data["S4AQ4A11"]

print("Distrubution of observations where either or both of above behaviors were noted")
print("2 - Both, 1 - One of the two, 0 - None/Unknown")
v2_1_counts = data["Restless_num"].value_counts(sort=False)
v2_1_perc = data["Restless_num"].value_counts(sort=False, normalize = True)
print(v2_1_counts)
print(sum(v2_1_counts))
print(v2_1_perc)

# Here I examine the population in my scope for age & gender

data_sub = data[(data["S4AQ4A5"].notnull())]
data_sub["CYEAR"] = pd.to_numeric(data_sub["CYEAR"])
data_sub["DOBY"] = pd.to_numeric(data_sub["DOBY"])

# Calculate age by subtracting date of birth from interview year

data_sub["AGE"] = data_sub["CYEAR"] - data_sub["DOBY"]

# Create age bins

def AGEBINS (row):
    if row['AGE'] < 21:
        return "0-20"
    elif row['AGE'] < 31:
        return "21-30"
    elif row['AGE'] < 41:
        return "31-40"
    elif row['AGE'] < 51:
        return "41-50"
    elif row['AGE'] < 61:
        return "51-60"
    elif row['AGE'] < 71:
        return "61-70"
    else:
        return "71+"
    
data_sub["AGEBINS"] = data_sub.apply (lambda row: AGEBINS(row), axis=1)
#print(data_sub["AGEBINS"].value_counts(sort=False))

# Create a histogram of AGE variable

seaborn.distplot(data_sub["AGE"].dropna(), kde=False);
plt.xlabel("Age of respondent")
plt.title("Age distribution")

# And here a binned histogram

seaborn.distplot(data_sub["AGE"].dropna(), kde=False, bins=20);
plt.xlabel("Age of respondent")
plt.title("Age distribution")

# These graphs will show the relation between my 4 categorical variables and respondents age
# Bar charts with age bins on x axis and categoricals on y axis

seaborn.factorplot(x="AGEBINS", y="S4AQ4A5", data=data_sub, kind="bar", ci=None, order = ["0-20","21-30","31-40","41-50","51-60","61-70","71+"]);
plt.xlabel("Age of respondent")
plt.ylabel("Percentage of 'Had trouble falling asleep'")

seaborn.factorplot(x="AGEBINS", y="S4AQ4A6", data=data_sub, kind="bar", ci=None, order = ["0-20","21-30","31-40","41-50","51-60","61-70","71+"]);
plt.xlabel("Age of respondent")
plt.ylabel("Percentage of 'Woke up too early'")

seaborn.factorplot(x="AGEBINS", y="S4AQ4A10", data=data_sub, kind="bar", ci=None, order = ["0-20","21-30","31-40","41-50","51-60","61-70","71+"]);
plt.xlabel("Age of respondent")
plt.ylabel("Percentage of 'Fidgeted/Paced'")

seaborn.factorplot(x="AGEBINS", y="S4AQ4A11", data=data_sub, kind="bar", ci=None, order = ["0-20","21-30","31-40","41-50","51-60","61-70","71+"]);
plt.xlabel("Age of respondent")
plt.ylabel("Percentage of 'Became uncomfortably restless'")
 