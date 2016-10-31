#!/usr/bin/env python
#-*- coding: utf-8 -*-
li = []
def checkio(li):
	otrali = []
	for numero in li:
		if li.count(numero) > 1:
			otrali.append(numero)
		else:
			otrali = otrali
	return otrali

print checkio([1, 2, 3, 1, 3]) #== [1, 3, 1, 3]
print checkio([1, 2, 3, 4, 5]) #== []
print checkio([5, 5, 5, 5, 5]) #== [5, 5, 5, 5, 5]
print checkio([10, 9, 10, 10, 9, 8]) #== [10, 9, 10, 10, 9]
