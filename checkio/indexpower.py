#!/usr/bin/env python
#-*- coding: utf-8 -*-
def index_power(li, N):
	resultado = 0		
	if N < len(li):
		resultado = li[N]**N
	else:
		resultado = -1
	return resultado

print index_power([1, 2, 3, 4], 2) #== 9
print index_power([1, 3, 10, 100], 3) #== 1000000
print index_power([0, 1], 0) #== 1
print index_power([1, 2], 3) #== -1
print index_power([1, 1, 1, 1, 1, 1, 1], 6) #Debería dar 1
