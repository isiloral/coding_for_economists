#Introducton to pandas and numpy
#pandas is a python library for data analysis and manipulation
import pandas as pd 
import numpy as np 
#If you get error while installing a package, try into shell: pip install PACKAGE_NAME

#lets look at pd.Series

#lets define our first pd.Series
ps = pd.Series([1, 'a', 2, np.pi])
print(ps)

#Which data type does our pd.Series have
print(type(ps))

#We can access the values
print(ps.values)
print(type(ps.values))

#accesss elements of pd.Series by indexing
print(ps[0:2])

#Define a custom index
series_1 = pd.Series(
  data = ["Schnitzel",'Lemonade','Whiskey'],
  index = ["Food", "Soda","Alcohol"])

#Advanced indexing of pd.Series
#using .loc[]
print(series_1.loc["Food"])

#using .iloc[]
series_1.iloc[0]

#Access elements from a range of indexes
print(series_1.loc["Food":"Alcohol"])

