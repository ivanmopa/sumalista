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
