# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 23:58:45 2023

@author: ANDREA DAZA
"""
#Sistemas de ecuaciones

import numpy as np
import math as ma

angulo_1 = ma.radians(2.92)
angulo_2 = ma.radians(33.8)
angulo_3 = ma.radians(47.9)
angulo_4 = ma.radians(78.8)
L = 15

a = np.array([[-ma.cos(angulo_1),-ma.sin(angulo_2)],[-ma.sin(angulo_1),ma.cos(angulo_2)]])
b = np.array([0.601*L*ma.sin(angulo_3)-1.02*L*ma.cos(angulo_4),0.601*L*ma.cos(angulo_3)+1.02*L*ma.sin(angulo_4)])

rta = np.linalg.solve(a,b)
print (rta)

#CHECK