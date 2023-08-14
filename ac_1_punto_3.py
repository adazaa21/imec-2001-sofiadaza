# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 22:59:55 2023

@author: ANDREA DAZA
"""
#Raíces

import pandas as pd
df = pd.read_csv('strain-stress.csv')
print (df)

#Planteamiento del problema
#1)crear lista con nuevos valores, de las dos ecuaciones dadas
#2)recorrer las listas para ver en qué valor coinciden

lista = df.values.tolist()
calculo = []

for i in lista:
    i = 23268*i+11
    calculo.append(i)
    
    
    
    
#for elemento_lista1 in lista1:
#for elemento_lista2 in lista2:
#if elemento_lista1 == elemento_lista2:
#           elementos_comunes.append(elemento_lista1)