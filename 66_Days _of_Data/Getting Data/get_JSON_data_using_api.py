# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 22:17:55 2021

@author: shubh
"""

import requests,json
import pandas as pd

data=requests.get("https://cat-fact.herokuapp.com/facts")

data=json.loads(data.content)

print(data)

print(type(data[0]))


cat=[]
ver=[]
x=None
y=None
for item in data:
    x=item['status']['verified']
    y=item['type']
    cat.append(y)
    ver.append(x)
    
cat=pd.Series(cat)
ver=pd.Series(ver)

dataframe=pd.concat([cat,ver],axis=1)

dataframe.to_csv('dataframe.csv',index=False)

xyz=pd.read_csv('dataframe.csv')