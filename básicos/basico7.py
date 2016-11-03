#!/usr/bin/env python
#-*- coding: utf-8 -*-
def diezveces(cadena):
	return cadena * 10

def holaadios(numero):
	if numero > 0:
		print 'hola'
	else: 
		print 'adios'

def suma(li):
	resultado = 0
	for elemento in li:
		resultado = resultado + elemento
	return "la suma es", resultado

def alreves(li):
	for elemento in li:
		li.reverse()
	return li
	
def parimpar(li):
	for numero in li:
		if numero%2 == 0:
			resultado = numero, 'El numero es par'
			print resultado
		else:
			resultado = numero, 'El numero es impar'
			print resultado
	return
