# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 18:19:12 2020

@author: jrena
"""
"""
Integrantes:
    Juan Renan Hernandez Luna
    Esmeralda Martinez Ronquillo
"""

tab=[]
tablero = [
	["0","0","0","0"],
	["0","0","0","0"],
	["0","0","0","0"],
	["0","0","0","0"]
    ]

solucion1=[]  
solucion2=[]  

reina= [0 for c in range(4)]        
libre = [True for r in range(4)]
diagonalabajo = [True for i in range(7)]       
diagonalarriba = [True for i in range(7)]

def reinas(c):
    global solucion1
    global solucion2
    global soluciones
    if c == 4:
        soluciones += 1 
        for r in range(4):
#            print (reina[r] + 1 ,end = " " if r<3 else "\n")
            tab.append(reina[r] + 1)
    else:       
        for r in range(4):
            if libre[r] and diagonalabajo[c + r] and diagonalarriba[ c+4-r]:
                reina[c] = r
                libre[r] = diagonalabajo[ c+r ] = diagonalarriba[ c+4-r ] = False
                reinas(c+1)
                libre[r] = diagonalabajo[ c+r ] = diagonalarriba[ c+4-r ] = True
    solucion1= tab[:4]
    solucion2= tab[4:]

def mostrar(t):
    for a in range(len(tablero)):
        for b in range (len(tablero[a])):
                tablero[a][b]=2
    diccionario = dict(enumerate(solucion1))
    for i in range (len(diccionario)):
        tablero[i][diccionario[i]-1] = 1
    for fila in tablero:
        for valor in fila:
            print("\t", valor, end=" ")
        print()
            

def mostrar2(t):    
    for a in range(len(tablero)):
        for b in range (len(tablero[a])):
                tablero[a][b]=2
    diccionario = dict(enumerate(solucion2))
    for i in range (len(diccionario)):
        tablero[i][diccionario[i]-1] = 1
    for fila in tablero:
        for valor in fila:
            print("\t", valor, end=" ")
        print()

soluciones = 0
reinas(0)
print("Las posibles soluciones son: ", soluciones)
print("Solucion: ")
mostrar(tablero)
print("Solucion: ")
mostrar2(tablero)



