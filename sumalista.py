#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Hacer una función que reciba una lista de números, sume solamente
#los positivos y devuelva el resultado de la cuenta.
def suma(numero):
	resultado = 0
	if numero >= 0:
		resultado = resultado + numero
		numero = raw_input('Introduce otro número: ')
	else:
		resultado = resultado
	return resultado
