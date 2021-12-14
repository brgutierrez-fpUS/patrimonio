# -*- coding: utf-8 -*-

from patrimonio import *


################################################################
#  Funciones de test
################################################################
def test_calcula_paises(registros):
    paises = calcula_paises(registros)
    print('Número de países con bienes Patrimonio de la Humanidad:', len(paises))

    
def test_bienes_por_tipo(registros):
    bienes_tipo = bienes_por_tipo(registros)
    print('\nNúmero de bienes por tipo:')
    for tipo in bienes_tipo:
        print('   ' , tipo, '-', len(bienes_tipo[tipo]))

    
def test_dibuja_bienes_por_tipo(registros):
    dibuja_bienes_por_tipo(registros)


def test_pais_mas_bienes(registros):
    numero_bienes, pais = pais_mas_bienes(registros)
    print('\nEl país con más bienes de tipo cultural es', pais, 'con', numero_bienes)
    numero_bienes, pais = pais_mas_bienes(registros, 'Natural')
    print('El país con más bienes de tipo natural es', pais, 'con', numero_bienes)

    
def test_bienes_mas_recientes_por_pais(registros):
    paises = ['Spain', 'France', 'Italy']
    bienes_pais = bienes_mas_recientes_por_pais(registros)
    print('\nTres bienes más recientes en España, Francia e Italia:')
    for pais in paises:
        print('   ' , pais, '-', bienes_pais[pais])

       
################################################################
#  Programa principal
################################################################
if __name__ == '__main__':
    registros = lee_bienes('../data/whs.csv')
    print("Número total de bienes:", len(registros)) 
    print(registros[:5], '\n')

    test_calcula_paises(registros)
    test_bienes_por_tipo(registros)
    test_dibuja_bienes_por_tipo(registros)
    test_pais_mas_bienes(registros)
    test_bienes_mas_recientes_por_pais(registros)
