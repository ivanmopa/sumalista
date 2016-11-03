#!/usr/bin/env python
#-*- coding: utf-8 -*-
li = [int(raw_input('Introduce un valor: ')), int(raw_input('Introduce otro: ')),
int(raw_input('Introduce uno más: '))]
for elemento in li:
	if elemento%2==0:
		print elemento, 'El número es par'
	else:
		print elemento, 'El número es impar'
