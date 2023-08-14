# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 22:51:51 2023

@author: ANDREA DAZA
"""
#Interpolación

#Para cuando x = 650
#Coordenadas punto 1:
x_0 = 645
y_0 = 6

#Coordenadas punto 2:
x_1 = 655
y_1 = 0

#Valor conocido de x:
x = 650

#Ecuación para interpolación:
y = (y_1-y_0)/(x_1-x_0)*(x-x_0)+y_0

#Resultado
#print("El valor de Y cuando X es:", x , "es :", y)

#Para cuando x = 580
#Coordenadas punto 1:
x_0 = 560
y_0 = 20

#Coordenadas punto 2:
x_1 = 620
y_1 = 12

#Valor conocido de x:
x = 580

#Ecuación para interpolación:
y = (y_1-y_0)/(x_1-x_0)*(x-x_0)+y_0

#Resultado
#print("El valor de Y cuando X es:", x , "es :", y)

#Para cuando x = 461
#Coordenadas punto 1:
x_0 = 455
y_0 = 26

#Coordenadas punto 2:
x_1 = 560
y_1 = 20

#Valor conocido de x:
x = 461

#Ecuación para interpolación:
y = (y_1-y_0)/(x_1-x_0)*(x-x_0)+y_0

#Resultado
print("El valor de Y cuando X es:", x , "es :", y)

#CHECK