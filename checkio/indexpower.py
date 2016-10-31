#!/usr/bin/env python
#-*- coding: utf-8 -*-
def index_power(li, N):
	resultado = 0
	for elemento in li:		
		if li.index(elemento)==N:
			resultado = elemento**N
		elif N > li.index(elemento):
			resultado = -1
	return resultado

#No vale porque si tienes dos valores iguales en la lista, li.index
#no sabe a cúal de los dos te estás refiriendo y siempre coge el
#que tiene el índice menor porque es en el orden en el que aparecen.
print index_power([1, 2, 3, 4], 2) #== 9
print index_power([1, 3, 10, 100], 3) #== 1000000
print index_power([0, 1], 0) #== 1
print index_power([1, 2], 3) #== -1
