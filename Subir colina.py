# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 13:54:31 2020

@author: jrena
"""

"""
Integrantes:
    Juan Renan Hernandez Luna
    Esmeralda Martinez Ronquillo
"""

from random import choice
import json

with open ("grafo.json","r") as read_file:
    data = json.load(read_file)

    camino=[]   
    
def buscar(inicio,valorBuscar):
    camino.append(inicio)
    comparacion = []
    comparacion2 = []
    aleatorio=[]
    aleatorio2=""
    mini = []
    mini2 = 0
    if inicio==valorBuscar:
        print ("Nodo encontrado")
    else:
        for i in data:
            if i[0] == inicio:
                comparacion.append(i)
                mini.append(i[2])
                mini2 = min(mini)
        for j in comparacion:
            if j[2] == mini2:
                comparacion2.append(j)
        if len(comparacion2)>1:
            for k in comparacion2:
                aleatorio.append(k[1])
                aleatorio2 = choice(aleatorio)
            return buscar(aleatorio2,valorBuscar)
        else:
            aleatorio2 = comparacion2[0][1]
        return buscar(aleatorio2,valorBuscar)
    
buscar ("A","M")
print(camino)







