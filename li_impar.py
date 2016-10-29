#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Hacer una función que reciba una lista, y devuelta otra lista 
#solamente con los elementos de indice impar.
li = []
def impar(li):
	otrali=[]
	for elemento in li:
		if elemento != li[1] and elemento != li[3] and elemento != li[5]:
			otrali.append(elemento)
		else:
			otrali = otrali
	return otrali
