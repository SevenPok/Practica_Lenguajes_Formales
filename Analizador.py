import re
import Metodos
import sys

def main():
	print("Practica 1 Lenguajes formales")
	while True:
		print(">> ", end="")
		entrada = input()
		if entrada.lower() == "exit":
			sys.exit()
		scan(entrada)

def scan(entrada):
	comando = str(entrada).lower()
	if 'solve' in comando and '[' in comando and ']' in comando:
		comando = cortar(comando)
		try:
			operar(comando)
		except :
			print("Syntax Error") 
	elif 'sum' in comando and '[' in comando and  ']' in comando:
		comando = cortar(comando)
		try:
			sum(comando)
		except :
			print("Syntax Error")
	else:
		print("Syntax Error")

def cortar(entrada):
	cadena = entrada.replace("solve", "")
	cadena = cadena.replace("[", "").replace("]", "")
	cadena = cadena.replace(" ", "")
	return entrada

def operar(entrada):
	patron = '\/\d*\.?\d+|\*\d*\.?\d+|\-\d*\.?\d+|\+\d*\.?\d+|\d*\.?\d+|\w+[(][^)]+[)]|\+\w+[(][^)]+[)]|\-\w+[(][^)]+[)]'
	cadena = re.findall(patron,entrada)

	solve = ""
	for i in cadena:
		if 'fact' in i:
			c = re.findall('\d+',i)
			n = Metodos.factorial(int(c[0]))
			if i[0:1] == '+' or i[0:1] == '-' or i[0:1] == '/' or i[0:1] == '*':
				solve = solve + i[0:1] + str(n)
			else:
				solve = solve + str(n)
		elif 'fib' in i:
			c = re.findall('\d+',i)
			n = Metodos.fibonacci(int(c[0]))
			if i[0:1] == '+' or i[0:1] == '-' or i[0:1] == '/' or i[0:1] == '*':
				solve = solve + i[0:1] + str(n)
			else:
				solve = solve + str(n)   
		elif 'ack' in i:
			c = re.findall('\d+',i)
			n = Metodos.ackermann(int(c[0]),int(c[1]))
			if i[0:1] == '+' or i[0:1] == '-' or i[0:1] == '/' or i[0:1] == '*':
				solve = solve + i[0:1] + str(n)
			else:
				solve = solve + str(n)
		elif 'exp' in i:
			c = re.findall('\d+|\-\d+|\+\d+',i)
			n = Metodos.exponente(int(c[0]),int(c[1]))
			if i[0:1] == '+' or i[0:1] == '-' or i[0:1] == '/' or i[0:1] == '*':
				solve = solve + i[0:1] + str(n)
			else:
				solve = solve + str(n)
		else:
			solve = solve + i
	print(eval(solve))

def sum(entrada):
	patron = '\d*\.?\d+|\-\d*\.?\d+'
	cadena = re.findall(patron, entrada)
	lista = []
	for i in cadena:
		lista.append(float(i))
	print(Metodos.suma(lista))

main()