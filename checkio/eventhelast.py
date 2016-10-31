#!/usr/bin/env python
#-*- coding: utf-8 -*-
def checkio(li):
	resultado = 0
	for elemento in li[::2]:
		resultado = resultado + elemento * li[-1]
	return resultado
	
print checkio([0, 1, 2, 3, 4, 5]) #== 30
print checkio([1, 3, 5]) #== 30
print checkio([6]) #== 36
print checkio([]) #== 0
