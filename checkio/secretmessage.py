#!/usr/bin/env python
#-*- coding: utf-8 -*-
def find_message(cadena):
	mensaje = cadena.replace(" ", "")
	minusculas = 'a'
	if cadena in minusculas:
		mensaje = cadena.remove(minusculas)
	
	return mensaje

print find_message("How are you? Eh, ok. Low or Lower? Ohhh.") #== "HELLO", "hello"
print find_message("hello world!") #== "", "Nothing"
print find_message("HELLO WORLD!!!") #== "HELLOWORLD", "Capitals"
