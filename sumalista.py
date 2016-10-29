#!/usr/bin/env python
#-*- coding: utf-8 -*-

#Hacer una función que reciba una lista de números, sume solamente
#los positivos y devuelva el resultado de la cuenta.
def suma(numero):
	resultado = 0
	while numero >= 0:
		resultado = resultado + numero
		numero = int(raw_input('Introduce otro número. Cuando te aburras, mete un número negativo: '))
	else:
		resultado = resultado
	return resultado
	
