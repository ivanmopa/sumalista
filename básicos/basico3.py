#!/usr/bin/env python
#-*- coding: utf-8 -*-
li = [int(raw_input('Introduce un valor: ')), int(raw_input('Introduce otro: ')),
int(raw_input('Introduce uno más: '))]
suma = 0
for elemento in li:
	suma = suma + elemento
print 'la suma es', suma
