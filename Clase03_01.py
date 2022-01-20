# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 18:03:30 2022

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
os.chdir("E:/RUBY/data science/quinta_profesora")
data = pd.read_csv("Banking.csv", header=0)

print(list(data.columns))
data["education"].unique()

data["education"]=np.where(data["education"] == "basic.4y","Basic", data["education"])
data["education"]=np.where(data["education"] == "basic.6y","Basic", data["education"])
data["education"]=np.where(data["education"] == "basic.9y","Basic", data["education"])

data["education"].unique()


##Check subcription porcentage


count_no_sub = len(data[data["y"]]==0)
count_sub = len(data[data["y"]==1])
pct_of_no_sub = count_no_sub/(count_no_sub+count_sub)
print("percentage of no subscription is", pct_of_no_sub*100)
pct_of_sub = count_sub/(count_no_sub+count_sub)
print("percentage of subcription", pct_of_sub*100)


data.groupby("y").mean()
#job, education, marital

sns.countplot(x="y", data=data, palette="Blues")
#plt.show()

data.insull().sum()

#job, marital,default

##customer job

sns.countplot(y="job", data=data, palette="GnBu_d")

sns.countplot(x="marital", data=data, palette="GnBu_d")
sns.countplot(x="default", data=data)
sns.countplot(x="housing", data=data, palette="cubehelix")
sns.countplot(x="loan", data=data)
sns.countplot(x="poutcome", data=data)

pd.crosstab(data.job,data.y).plot(kind="bar")
plt.title("Purchase Frequency for Job Title")
plt.xlabel("Job")
plt.ylabel("Frequency of Purchase")
plt.savefig("purchase_freq_job")

table=pd.crosstab(data.marital,data.y)
table.div(table.sum(1).astype(float),axis=0).plot(kind="bar", stacked=True)
plt.title("Stacked Bar Chart of Marital Status Vs. Purchase")
Plt.xlabel("Marital Status")
plt.ylabel("Proportion of customers")
plt.savefig("marital_vs_pur_stack")
##daltan las otras variables

###pd.crosstab(data.month,data.y).plot(kind="bar")
plt.title("Purchase Frequency for Month")
plt.xlabel("Month")
plt.ylabel("Frequency of Purchase")
plt.savefig("pur_fre_month_bar")


pd.crosstab(data.month,data.y).plot(kind="bar")
plt.title("Purchase Frequency for Month")
plt.xlabel("Month")
plt.ylabel("Frequency of Purchase")
plt.savefig("pur_fre_month_bar")


data.age.hist()
plt.title("Histogram of Age")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.savefig("hist_age")


pd.crosstab(data.poutcome,data.y).plot(kind="bar")
plt.title("Purchase Frequency for poutcome")
plt.xlabel("Poutcome")
plt.ylabel("Frequency of Purchase")
plt.savefig("pur_fre_pout_bar")
##

data.drop(data.columns[[0,3,7,8,9,10,11,12,13,15,16,17,18,19]], axis=1, inplace=True)

data2 = pd.get_dummies(data,columns=["job","marital","default","housing", "loan", "poutcome"])
data2 = drop(data2.columns[[12, 16, 18, 21, 24]], axis=1, inplace=True)
data2.columns
sns.heatmap(data2.corr())

X = data2.iloc[:,1:]
y = data2.iloc[:,0]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
X_train.shape

classifier = LogisticRegression(random_state=0)
classifier.fit(X_train,y_train)

y_pred=classifier.predict(X_test)
probability = classifier.predict_proba(X_test)
print(probability)


from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)

print ("Accuracy of Logistic Regression classifier on test set:{:.2f}" . format(classifier.score(X_test, y_test)))
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))





from sklearn.metrics import 
