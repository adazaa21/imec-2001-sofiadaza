# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 11:32:02 2023

@author: ANDREA DAZA
"""
#Ajuste de datos

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_excel('engines.xlsx')
#print (df)

rev = df['Revolutions per Minute (RPM)'].values.reshape(-1,1)
mass = df['Mass (Kg)'].values.reshape(-1,1)
linear_regressor = LinearRegression()
linear_regressor.fit(mass,rev)
final = linear_regressor.predict(mass)

fig = plt.figure(figsize= (14,14))
plt.scatter(df['Revolutions per Minute (RPM)'],df['Mass (Kg)'])
plt.plot(df['Revolutions per Minute (RPM)'],df['Mass (Kg)'])
plt.plot(mass, rev, color = 'red')
plt.ylabel('Revolutions per Minute (RPM)')
plt.xlabel('Mass (kg)')
plt.grid()


#ecuacion = mx + b
m = linear_regressor.coef_[0][0]
b = linear_regressor.intercept_[0]

#CHECK