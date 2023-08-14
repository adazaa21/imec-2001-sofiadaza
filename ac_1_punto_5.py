# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 00:20:58 2023

@author: ANDREA DAZA
"""

#Optimización

#importas libreria
import csv
#utilizas el nombre del archivo
filename= "Archivos/strain-stress.csv"
text=open(filename,"r")
text="".join([i for i in text]).replace(";",",")
x=open("output.csv","w")
x.writelines(text)
x.close()
#Abres el archivo y lo lees con ayuda de pandas
with open("output.csv","r") as file:
    reader= csv.reader(file)
    data=[]
    for row in reader:
        data.append(row)

#Nueva función
i=1
for i in range(1,len(data)):
    ref=data[i]
    strain=float(ref[0])
    o_elastica=(23268*strain)+11
    o_plastica=(26202*(strain*3))-(11347(strain*2))+(1332(strain))+78
    if o_elastica==o_plastica:
        rta= o_plastica
    else:
        rta=None
    print(ref)
print(rta)