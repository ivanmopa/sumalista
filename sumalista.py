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

#Este no recibe una lista de números (de las que se ponen entre corchetes).
#Tenía dudas si te referías a una lista de esas o a esto, que también lo
#considero lista al ser una sucesión de números. Al final he pensado que 
#esto ya lo hiciste tú en clase, por eso he hecho el otro.
