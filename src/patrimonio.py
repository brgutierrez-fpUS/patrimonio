# -*- coding: utf-8 -*-
''' Bienes Patrimonio de la Humanidad 

AUTOR: Mariano González
REVISOR: José A. Troyano, Fermín Cruz, Carlos García
ÚLTIMA MODIFICACIÓN: 7/12/2019

En este ejercicio trabajaremos sobre el dataset de Bienes Patrimonio
de la Humanidad, http://whc.unesco.org/en/list/. Este dataset contiene
registros de los bienes declarados Patrimonio de la Humanidad.
Los datos están en formato CSV. Estas son las primeras líneas
del fichero de entrada:

    id,name,year,category,country
    1,Galápagos Islands,1978,Natural,Ecuador
    2,City of Quito,1978,Cultural,Ecuador
    3,Aachen Cathedral ,1978,Cultural,Germany
    4,L’Anse aux Meadows National Historic Site,1978,Cultural,Canada
    8,Ichkeul National Park,1980,Natural,Tunisia
    9,Simien National Park,1978,Natural,Ethiopia
    10,Lower Valley of the Awash,1980,Cultural,Ethiopia
        
FUNCIONES DISPONIBLES:
----------------------
- lee_bienes(fichero):
    lee el fichero de bienes
- calcula_paises(registros):
    calcula el conjunto de países que poseen bienes
- bienes_por_tipo(registros):
    calcula los bienes de cada tipo (Cultural, Natural, Mixed)
- dibuja_bienes_por_tipo(registros):
    dibuja un diagrama de barras con el número de bienes de cada tipo    
- pais_mas_bienes(registros, tipo):
    calcula el país con mayor número de bienes de un tipo dado
- bienes_mas_recientes_por_pais(registros, n=3):
    calcula los n bienes más recientes de cada país
'''

import csv
from matplotlib import pyplot as plt
from collections import Counter
from collections import namedtuple

Bien = namedtuple('Bien', 'code, name, year, category, country') 
    
# EJERCICIO 1:
def lee_bienes(fichero):
    ''' Lee el fichero de bienes
        Devuelve una lista de tuplas, donde cada tupla contiene las
        cinco propiedades de un bien, en el mismo orden en que
        aparecen en el fichero y con el tipo de dato adecuado
        
        ENTRADA:
        - fichero: el nombre del fichero csv -> str
        
        SALIDA:
        - Lista de tuplas con la información del csv
            -> [(int, str, int, str, str)]
    '''
    pass


# EJERCICIO 2:
def calcula_paises(registros):
    ''' Calcula el conjunto de países que poseen bienes
        Devuelve un conjunto con los nombres de los países
        
        ENTRADA:
        - registros: lista de tuplas con información de bienes
            -> [(int, str, int, str, str)]
        
        SALIDA:
        - Conjunto de nombres de países -> {str}
    '''
    pass


# EJERCICIO 3:
def bienes_por_tipo(registros):
    ''' Calcula los bienes de cada tipo (Cultural, Natural, Mixed)
        Devuelve un diccionario cuyas claves son los tipos de bienes
        y cuyos valores son listas de tuplas con los bienes de cada tipo
        
        ENTRADA:
        - registros: lista de tuplas con información de bienes
            -> [(int, str, int, str, str)]
        
        SALIDA:
        - Diccionario de bienes por tipo -> {str:[(int, str, int, str, str)]}
    '''
    pass


# EJERCICIO 4:
def dibuja_bienes_por_tipo(registros):
    ''' Dibuja un diagrama de barras con el número de bienes de cada tipo
    
        Para dibujar las barras, utilice las siguientes instrucciones:
            plt.barh(range(len(numero_bienes)), numero_bienes, tick_label=tipos)
            plt.show()
        donde numero_bienes es una lista con el número de bienes de cada tipo,
        y tipos es una lista con los nombres de los tipos de bienes
        
        ENTRADA:
        - registros: lista de tuplas con información de bienes
            -> [(int, str, int, str, str)]        
    '''
    pass

    
# EJERCICIO 5:
def pais_mas_bienes(registros, tipo_bien='Cultural'):
    ''' Calcula el país con mayor número de bienes de un tipo dado
        Devuelve una tupla con el número de bienes y el nombre del país
        
        ENTRADA:
        - registros: lista de tuplas con información de bienes
            -> [(int, str, int, str, str)]
        - tipo_bien: el tipo de bienes para el que se realizará la operación
            -> str
        
        SALIDA:
        - Tupla con el número de bienes y el nombre del país -> (int, str)
    '''
    pass


# EJERCICIO 6:
def bienes_mas_recientes_por_pais(registros, n=3):
    ''' Calcula los n bienes más recientes de cada país
        Devuelve un diccionario cuyas claves son los países
        y cuyos valores son listas de tuplas con el año y el nombre
        de los n bienes más recientes de cada país,
        en orden decreciente del año
        
        ENTRADA:
        - registros: lista de tuplas con información de bienes
            -> [(int, str, int, str, str)]
        
        SALIDA:
        - Diccionario de bienes por país
            -> {str: [(int, str)]}
    ''' 
    pass