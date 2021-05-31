# -*- coding: utf-8 -*-
"""
Created on Sun May 28 21:22:24 2021

@author: Hp
"""

#importando librerias
import pandas as pd
#network para grafos
import networkx as nx
#lectura de datos
datos=pd.read_csv('rutas.csv',sep=';',header=0)
#mostrando datos
print(datos)
#grafo
dirgrafo=nx.DiGraph()
for row in datos.iterrows():
    dirgrafo.add_edge(row[1]["origen"],
                row[1]["destino"],
                duration=row[1]["peso"])
#camino mas corto 
print("")
#print(list(nx.all_shortest_paths(dirgrafo,source="a", target="e", weight=None)))
#print(list(nx.dijkstra_path(dirgrafo,source="a", target="e", weight="peso")))
#lectura de filas del csv
#print(datos.iloc[0]["origen"])
#print(datos.iloc[0]["destino"])
#print(datos.iloc[0:4]["peso"])
filas_conteo=len(datos.axes[0])
#print(filas_conteo)
vector_distancia=[]
vector_destino=[]
pesoTotal=100
datoMen=""
a=1
i=0
dato=""
peso=0
if a==1:
    vector_destino.append(datos.iloc[i]["origen"])
    a=2
    i=1
    for j in range(filas_conteo):
        if vector_destino[i-1] == datos.iloc[j]["origen"]:
            dato=datos.iloc[j]["destino"]
            peso=datos.iloc[j]["peso"]
        if pesoTotal > peso:
            pesoTotal=peso
            datoMen=dato
    vector_destino.append(datoMen)
    i=2
pesoTotal=100
peso=100
for j in range(filas_conteo):
        if vector_destino[i-2]!=datos.iloc[j]["origen"]:
            if vector_destino[i-1] == datos.iloc[j]["origen"] and vector_destino[i-2]!=datos.iloc[j]["destino"] :
                dato=datos.iloc[j]["destino"]
                peso=datos.iloc[j]["peso"]
        if pesoTotal > peso:
            pesoT=peso
            datoMen=dato
vector_destino.append(datoMen)
i=3
pesoTotal=100
peso=100
for j in range(filas_conteo):
        if vector_destino[i-3]!=datos.iloc[j]["origen"] and vector_destino[i-2]!=datos.iloc[j]["origen"] :
            if vector_destino[i-1]==datos.iloc[j]["origen"] :
                if vector_destino[i-3]!=datos.iloc[j]["destino"] and vector_destino[i-2]!=datos.iloc[j]["destino"] and vector_destino[i-1]!=datos.iloc[j]["destino"]:
                    dato=datos.iloc[j]["destino"]
                    peso=datos.iloc[j]["peso"]                                
            if pesoTotal > peso:
                pesoTotal=peso
                datoMen=dato            
vector_destino.append(datoMen)
i=4
pesoTotal=100
peso=100                   
for j in range(filas_conteo):
        if vector_destino[i-4]!=datos.iloc[j]["origen"] and vector_destino[i-3]!=datos.iloc[j]["origen"] and vector_destino[i-2]!=datos.iloc[j]["origen"] :
            if vector_destino[i-1]==datos.iloc[j]["origen"] :
                if vector_destino[i-4]!=datos.iloc[j]["destino"] and vector_destino[i-3]!=datos.iloc[j]["destino"] and vector_destino[i-2]!=datos.iloc[j]["destino"] and vector_destino[i-1]!=datos.iloc[j]["destino"]:
                    dato=datos.iloc[j]["destino"]
                    peso=datos.iloc[j]["peso"]                    
            if pesoTotal > peso:
                pesoTotal=peso
                datoMen=dato     
vector_destino.append(datoMen)           
res=[]
for i in vector_destino:
    res.append(i)
print("la ruta mas corta es :")
print(res)