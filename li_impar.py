#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Hacer una función que reciba una lista, y devuelta otra lista 
#solamente con los elementos de indice impar.
def impar(li):
	li = ['hola', 247, 474, 'Pakito', True, 'Belén Esteban', 'tortilla']
	otrali=[]
	for elemento in li:
		if elemento != li[2][4][6]:
			otrali.append(elemento)
		else:
			otrali = otrali
	return otrali
