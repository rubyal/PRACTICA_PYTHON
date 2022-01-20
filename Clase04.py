# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 19:22:39 2022

@author: ruby_
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rc("font", size=14)
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)
import os 
os.chdir("E:\RUBY\data science\quinta_profesora")
data=pd.read_csv("Winequality.csv", sep=";")

print(list(data.columns))
print(data)

data2= data.str.split(";")