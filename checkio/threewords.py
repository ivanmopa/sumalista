#!/usr/bin/env python
#-*- coding: utf-8 -*-
def checkio(cadena):
	li = cadena.split()
	cuenta = 0
	espalabra = False
	for palabra in li:
		if palabra not in "123456789":
			cuenta = cuenta + 1
			if cuenta >= 3:
				espalabra = True
		else:
			espalabra = espalabra
	return espalabra

print checkio("Hello World hello") #== True
print checkio("He is 123 man") #== False
print checkio("1 2 3 4") #== False
print checkio("bla bla bla bla") #== True
print checkio("Hi") #== False
print checkio("hola 123 pepe 3484 jose 47838") #Debería dar False
print checkio("jeje 1484 hola me llamo 245") #Debería dar True
