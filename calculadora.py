#!/usr/bin/python3

import sys


def calcular(numero1,numero2,operacion):
	try:
		numero1 = int(numero1)
		numero2 = int(numero2)
		if operacion == 'suma':
			print(numero1,'+',numero2,'=',numero1+numero2)
			return numero1+numero2
		elif operacion == 'resta':
			print(numero1,'-',numero2,'=',numero1-numero2)
			return numero1-numero2
		elif operacion == 'multiplicacion':
			print(numero1,'*',numero2,'=', numero1*numero2)
			return numero1*numero2
		elif operacion == 'division':
			try:
				print(numero1,'/',numero2,'=',numero1/numero2)
				return numero1/numero2
			except:
				print("ERROR:Estas intentando divir entre 0") 
				return "division incorrecta"
		else: 
 			print('Operacion mal escrita\nLos tipos de operacion son : suma , resta, multiplicacion,division') 
 			return'Operacion mal escrita\nLos tipos de operacion son : suma , resta, multiplicacion,division'
	except: 
		print('ERROR:',numero1,'y',numero2,'deben de ser float') 

if __name__ == "__main__":
	if len(sys.argv) != 4:
		sys.exit("Numero de Argumentos invalido")
	else:
		operacion = sys.argv[1]
		numero1 = sys.argv[2]
		numero2 = sys.argv[3]
		print("El resultado final es: ",calcular(numero1,numero2,operacion))
