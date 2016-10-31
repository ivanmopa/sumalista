#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Hacer una función que reciba una lista, y devuelta otra lista 
#solamente con los elementos de indice impar.
li = []
def impar(li):
	otrali=[]
	for elemento in li:
		otrali = li[1::2]
	return otrali

#Si miras el commit anterior, verás que la estaba liando pardísima y que estaba
#complicando el código de una manera increíble. Así está mucho más simplificado.


print impar([32, 'pakito', 'chorizo', 1300, 233, 'tortilla']) #Debería dar ['pakito', 1300, 'tortilla']
print impar(['hola', True, 'Jacinto', 2458, 14]) #Debería dar [True, 2458]
print impar(['nada']) #Debería dar []
print impar([False, 13, 45, True, 248, True, 458, 13]) #Debería dar [13, True, True, 13]
print impar([1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1]) #Debería dar [1, 1, 1, 1, 1, 1]

#Nota mental: li[1::2] significa que vaya desde la posición 1 hasta el final. Y
#con el último :2 estoy indicando el espacio entre salto y salto. Es decir,
#que vaya desde la posición 1 hasta el final saltando los índices pares.

