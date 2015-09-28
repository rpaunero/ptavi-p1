#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

def suma(operando1, operando2):
	return operando1 + operando2

def rest(operando1, operando2):
	return operando1 - operando2

def mult(operando1, operando2):
	return operando1 * operando2

def div(operando1, operando2):
	return operando1 / operando2

if __name__ == "__main__":
	try:
		operando1 = int(sys.argv[1])
		operador = sys.argv[2]
		operando2 = int(sys.argv[3])
	
	except ValueError:
		sys.exit("INTRODUCIR [NUMERO] [OPERADOR] [NUMERO]")

	if sys.argv[2] == "suma":
		print(suma(operando1, operando2))
	elif sys.argv[2] == "resta":
		print(rest(operando1, operando2))
	elif sys.argv[2] == "mult":
		print(mult(operando1, operando2))
	elif sys.argv[2] == "div":
			if operando2 == 0:
				sys.exit("INDETERMINACIÓN")
			else:
				print(div(operando1, operando2))
	else:
		sys.exit("OPERADOR NO DEFINIDO")
