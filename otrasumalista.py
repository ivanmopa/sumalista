#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Hacer una función que reciba una lista de números, sume solamente
#los positivos y devuelva el resultado de la cuenta.
li = []
def suma(li):
	resultado = 0
	for numero in li:
		if numero > 0:
			resultado = resultado + numero
		else:
			resultado = resultado
	return resultado

print suma([10, 10, 10, -10]) #Debería dar 30
print suma([-3, -4, -5, 6]) #Debería dar 6
print suma([4, -1, 8, -5, 9, -4]) #Debería dar 21
print suma([3, 4, -5, 4, 3]) #Debería dar 14

