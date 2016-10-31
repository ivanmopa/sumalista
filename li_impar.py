#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Hacer una función que reciba una lista, y devuelta otra lista 
#solamente con los elementos de indice impar.
li = []
def impar(li):
	otrali=[]
	for elemento in li:
		if li.index(elemento)%2==0:
			otrali = otrali
		else:
			otrali.append(elemento)
	return otrali

print impar([32, 'pakito', 'chorizo', 1300, 233, 'tortilla']) #Debería dar ['pakito', 1300, 'tortilla']
print impar(['hola', True, 'Jacinto', 2458, 14]) #Debería dar [True, 2458]
print impar(['nada']) #Debería dar []
print impar([False, 13, 45, True, 248, True, 458, 13]) #Debería dar [13, True, True, 13]
print impar([1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1]) #Debería dar [1, 1, 1, 1, 1, 1]
#Haciendo un ejercicio de Checkio me di cuenta de que li.index solo tenía en cuenta
#el primer índice que encontraba cuando se repetían dos valores. Así que al añadir
#esta última prueba, me he dado cuenta de que falla. 
