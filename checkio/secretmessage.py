#!/usr/bin/env python
#-*- coding: utf-8 -*-
def find_message(cadena):
	mayusculas = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
	mensaje = ''
	li = []
	for letra in cadena:
		if letra in mayusculas:
			li.append(letra)
	for elemento in li:
		mensaje = ''.join(li)
	return mensaje

print find_message("How are you? Eh, ok. Low or Lower? Ohhh.") #== "HELLO", "hello"
print find_message("hello world!") #== "", "Nothing"
print find_message("HELLO WORLD!!!") #== "HELLOWORLD", "Capitals"

#El método ''.join lo que hace es unir elementos de una lista separados por comas.
#Si en vez de ''.join pongo ' '.join, los une con un espacio en medio.
#Y si pongo '_'.join, los une con una barra baja en medio.
