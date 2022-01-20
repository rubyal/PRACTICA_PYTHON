# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 20:01:53 2022

@author: ruby_
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets 

os.chdir('E:\RUBY\data science\quinta_profesora')
plt.style.use('ggplot')

wine_df = pd.read_csv('Winequality.csv', sep = ';')
X = wine_df.drop('quality', axis=1).values 
y = wine_df['quality'].values

pd.DataFrame.hist(wine_df,figsize = [15,15], color = 'red')

plt.figure(figsize=(20,5));
plt.subplot(1,2,1);
plt.hist(y,color='maroon');
plt.xlabel('original target value');
plt.ylabel('count');
plt.subplot(1,2,2);
plt.hist(y,color='navy');
plt.xlabel('aggregated target value');
plt.show()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=42)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))
X_train = scaler.fit_transform(X_train)
X_train = pd.DataFrame(X_train)
X_test = scaler.fit_transform(X_test)
X_test = pd.DataFrame(X_test)


from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import mean_squared_error

knn = KNeighborsClassifier(n_neighbors=27)
knn.fit(X_train, y_train)


y_pred = knn.predict(X_test)
from sklearn import metrics

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))





