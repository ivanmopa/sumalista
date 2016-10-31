#!/usr/bin/env python
#-*- coding: utf-8 -*-
def checkio(cadena):
	li = []
	cuenta = 0
	for letras in cadena:
		li = cadena.split()
	for palabra in li:
		if palabra not in '0123456789':
			cuenta = cuenta + 1
	return cuenta

print checkio("Hello World hello") #== True
print checkio("He is 123 man") #== False
print checkio("1 2 3 4") #== False
print checkio("bla bla bla bla") #== True
print checkio("Hi") #== False
