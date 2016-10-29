#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Hacer una función que reciba una lista, y devuelta otra lista 
#solamente con los elementos de indice impar.
def impar(ele1, ele2, ele3, ele4, ele5, ele6):
	li = [ele1, ele2, ele3, ele4, ele5, ele6]
	otrali=[]
	for elemento in li:
		if elemento != li[1] and elemento != li[3] and elemento != li[5]:
			otrali.append(elemento)
		else:
			otrali = otrali
	return otrali
