# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 21:25:26 2022

@author: ruby_
"""

import pandas as pd
import numpy as np
from sklearn import preprocessing
import matplotlib.pyplot as plt
plt.rc("font", size=14)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import seaborn as sns 
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
import os
os.chdir('E:\RUBY\data science\quinta_profesora')
plt.style.use('ggplot')
social = pd.read_csv('Social_Network_Ads.csv', sep = ',')
print(list(social.columns))

count_no_sub=len(social[social["Purchased"]==0])
count_sub = len(social[social["Purchased"]==1])
pct_of_no_sub=count_no_sub/(count_no_sub+count_sub)
print("percentage of no buy is", pct_of_no_sub*100)
pct_of_sub = count_sub/(count_no_sub+count_sub)
print("percentage of buy", pct_of_sub*100)


social.groupby("Purchased").mean()

##sns.countplot(x="y", data=data, palette="Blues")


social.insull().sum()

sns.countplot(y="job", data=data, palette="GnBu_d")
sns.countplot(x="marital", data=data, palette="GnBu_d")
sns.countplot(x="default", data=data)
sns.countplot(x="housing", data=data, palette="cubehelix")
sns.countplot(x="loan", data=data)
sns.countplot(x="poutcome", data=data)

########

social["Purchased"].value_counts().plot(kind="bar")


sns.countplot(x='Purchased', social=social, palette="Blues")

social.insull().sum()