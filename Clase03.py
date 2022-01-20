# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 19:08:07 2022

@author: ruby_

"""

import pandas as pd #for data analysis
import numpy as np #numerical data funcionality
import matplotlib.pyplot #plotting graphs. data visualization library
import os #opertive system stuff
import csv 

os.chdir("E:\RUBY\data science\quinta_profesora")
cwd = os.getcwd()
print(cwd)


data= pd.read_csv("Banking.csv")
data
age=data["age"] ##numerica
job=data["job"] ##categorica
## variable si y no categorica

data["education"].unique()
data[""]




plt.bar(age,job)














file=open("Banking.csv")
type(file)

csvreader = csv.reader(file)


rows = []
for row in csvreader:
        rows.append(row)
rows




##
import pandas as pd #for data analysis
import numpy as np #numerical data funcionality
import matplotlib.pyplot #plotting graphs. data visualization library
import os #opertive system stuff
import csv 

