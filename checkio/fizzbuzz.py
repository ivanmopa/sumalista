#!/usr/bin/env python
#-*- coding: utf-8 -*-
def checkio(numero):
	if numero%3==0 and numero%5==0:
		resultado = "Fizz Buzz"
	elif numero%3==0:
		resultado = "Fizz"
	elif numero%5==0:
		resultado = "Buzz"
	else:
		resultado = str(numero)	
	return resultado

print checkio(15) #== "Fizz Buzz"
print checkio(6) #== "Fizz"
print checkio(5) #== "Buzz"
print checkio(7) #== "7"
