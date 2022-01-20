# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 20:57:19 2021

@author: ruby_
"""

import pandas as pd #for data analysis
import numpy as np #numerical data funcionality
import matplotlib.pyplot #plotting graphs. data visualization library
import os #opertive system stuff

#set working directory

os.chdir("E:\RUBY\data science\quinta_profesora")
cwd = os.getcwd()
print(cwd)

##importar archivo de datos
excel_file="Movies.xls"  #this is a flag
movies=pd.read_excel(excel_file) #Dataframe object
movies.head(15) #ver entradas iniciales
movies.tail(15) #ver entradas finales

movies_sheet1= pd.read_excel(excel_file, sheet_name=0, index_col=0)
movies_sheet2= pd.read_excel(excel_file, sheet_name=1, index_col=0)
movies_sheet3= pd.read_excel(excel_file, sheet_name=2, index_col=0)
movies=pd.concat([movies_sheet1, movies_sheet2, movies_sheet3]) #poner todas las hojas en un solo dataframe
movies.shape #contar las filas y columnas

sorted_by_gross=movies.sort_values(["Gross Earnings"], ascending="False") #organizar los datos según la variable que se quiera
sorted_by_gross["Gross Earnings"].head(10)
sorted_by_gross["Gross Earnings"].head(10).plot(kind="barh")
##plt.show()##mostrar el grafico

movies["IMDB Score"].plot(kind="hist")

#1 code (volver hacerlo)
# distribuciones de distintas variables
#diagrama de barras y histograma (3cada una)


##################
os.chdir("E:\RUBY\data science\quinta_profesora")
cwd = os.getcwd()
print(cwd)

##importar archivo de datos
excel_file="Movies.xls"  #this is a flag
movies=pd.read_excel(excel_file) #Dataframe object
movies.head(15) #ver entradas iniciales
movies.tail(15) #ver entradas finales

movies_sheet1= pd.read_excel(excel_file, sheet_name=0, index_col=0)
movies_sheet2= pd.read_excel(excel_file, sheet_name=1, index_col=0)
movies_sheet3= pd.read_excel(excel_file, sheet_name=2, index_col=0)
movies=pd.concat([movies_sheet1, movies_sheet2, movies_sheet3]) #poner todas las hojas en un solo dataframe
movies.shape #contar las filas y columnas

sorted_by_gross=movies.sort_values(["Duration"], ascending="False") #organizar los datos según la variable que se quiera
sorted_by_gross["Duration"].head(10)
sorted_by_gross["Duration"].head(10).plot(kind="barh")
##plt.show()##mostrar el grafico

movies["Duration"].plot(kind="hist")

##################
os.chdir("E:\RUBY\data science\quinta_profesora")
cwd = os.getcwd()
print(cwd)

##importar archivo de datos
excel_file="Movies.xls"  #this is a flag
movies=pd.read_excel(excel_file) #Dataframe object
movies.head(15) #ver entradas iniciales
movies.tail(15) #ver entradas finales

movies_sheet1= pd.read_excel(excel_file, sheet_name=0, index_col=0)
movies_sheet2= pd.read_excel(excel_file, sheet_name=1, index_col=0)
movies_sheet3= pd.read_excel(excel_file, sheet_name=2, index_col=0)
movies=pd.concat([movies_sheet1, movies_sheet2, movies_sheet3]) #poner todas las hojas en un solo dataframe
movies.shape #contar las filas y columnas

sorted_by_gross1=movies.sort_values(["Facebook Likes - Actor 1"], ascending="False") #organizar los datos según la variable que se quiera
sorted_by_gross["Facebook Likes - Actor 1"].head(10)
sorted_by_gross["Facebook Likes - Actor 1"].head(10).plot(kind="barh")
##plt.show()##mostrar el grafico

movies["Aspect Ratio"].plot(kind="hist")

##################
os.chdir("E:\RUBY\data science\quinta_profesora")
cwd = os.getcwd()
print(cwd)

##importar archivo de datos
excel_file="Movies.xls"  #this is a flag
movies=pd.read_excel(excel_file) #Dataframe object
movies.head(15) #ver entradas iniciales
movies.tail(15) #ver entradas finales

movies_sheet1= pd.read_excel(excel_file, sheet_name=0, index_col=0)
movies_sheet2= pd.read_excel(excel_file, sheet_name=1, index_col=0)
movies_sheet3= pd.read_excel(excel_file, sheet_name=2, index_col=0)
movies=pd.concat([movies_sheet1, movies_sheet2, movies_sheet3]) #poner todas las hojas en un solo dataframe
movies.shape #contar las filas y columnas

sorted_by_gross1=movies.sort_values(["Facebook Likes - Actor 1"], ascending="False") #organizar los datos según la variable que se quiera
sorted_by_gross["Facebook Likes - Actor 1"].head(10)
sorted_by_gross["Facebook Likes - Actor 1"].head(10).plot(kind="barh")
##plt.show()##mostrar el grafico

movies["Users votes"].plot(kind="hist")


####""###

movies.describe()
movies["Gross Earnings"].mean()
movies["Gross Earnings"].corr(movies['Budget'])

#Get Net Earnings:

movies["Net Earnings"]=movies["Gross Earnings"]-movies["Budget"]
sorted_movies=movies[["Net Earnings"]].sort_values(["Net Earnings"], ascending=False)
sorted_movies.head(10)['Net Earnings'].plot.barh()

movies_subset=movies [["Year","Gross Earnings"]]
movies_subset.head()
earnings_by_year=movies_subset.pivot_table(index=["Year"])
earnings_by_year.head()
earnings_by_year.plot()

movies_subset1=movies[["Country","Language","Gross Earnings"]]
movies_subset.head()

earnings_by_co_lang = movies_subset1.pivot_table(index=['Country','Language'])
earnings_by_co_lang.head()
earnings_by_co_lang.head(20).plot(kind="bar", figsize=(20,8))

earnings_by_co_lang.to_excel("output.xlsx")

##ejercicio###

movies.describe()
movies["Duration"].mean()
movies["Duration"].corr(movies["Aspect Ratio"])
movies["Duration"].corr(movies["Gross Earnings"])
movies["Duration"].corr(movies["Budget"])
movies["Duration"].corr(movies["Reviews by Crtiics"])

#movies likes
movies["Reviews"]= movies["Reviews by Users"] + movies["Reviews by Crtiics"]

sorted_movies=movies[["Reviews"]].sort_values(["Reviews"],ascending=False)
sorted_movies.head(10)['Reviews'].plot.barh()

movies_subset3=movies [["Director","Duration", "Reviews by Users"]]
movies_subset3.head()
earnings_by_year=movies_subset3.pivot_table(index=["Director"])
earnings_by_year.head()
earnings_by_year.plot()

movies_subset1=movies[["Director","Duration", "Reviews by Users"]]
movies_subset1.head()

earnings_by_co_lang = movies_subset1.pivot_table(index=["Director","Duration"])
earnings_by_co_lang.head()
earnings_by_co_lang.head(10).plot(kind="bar", figsize=(20,8))

earnings_by_co_lang.to_excel("director.xlsx")

