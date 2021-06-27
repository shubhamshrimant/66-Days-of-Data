# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 10:15:06 2021

@author: shubh
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv("C:\\Users\\shubh\\Desktop\\BTC-USD.csv")

data.info()


data.isna().sum()

data=data.dropna()

data.Open.groupby(data.Open).value_counts()

data.value_counts()

xyz=data.head()
#plt.plot(data.Close,data.Open)

#plt.bar(xyz.Date,xyz.Open,color='r')

#plt.bar(xyz.Date,xyz.Close,color='g')

#plt.show()

data['Date'] = pd.to_datetime(data.Date,format='%Y-%m-%d')
data.index = data['Date']

plt.figure(figsize=(16,8))
plt.plot(data['Close'], label='Close Price history')
