import re
import Metodos
import sys

def main():
	print("Practica 1 Lenguajes formales")
	while True:
		print(">> ", end="")
		cadena = input()
		if cadena.lower() == "exit":
			sys.exit()
		scan(cadena)

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
	elif 'sort' in comando and '--type=':
		comando = cortar(comando)
		try:
			sort(comando)
		except :
			print("Syntax Error")
		pass
	elif 'drawtriangle' in comando and '--type=asc' in comando and '--length=' in comando:
		try:
			triangle(comando)
		except :
			print("Syntax Error")
	elif 'drawtriangle' in comando and '--type=desc' in comando and '--length=' in comando:
		try:
			triangleDes(comando)
		except :
			print("Syntax Error")
	elif 'drawrhombus' in comando and '--size=' in comando:
		try:
			rombo(comando)
		except :
			print("Syntax Error")
	elif 'exec' in comando and '--file=' in comando:
		try:
			documento(exec(comando))
		except:
			print("Syntax Error")
	else:
		print("Syntax Error")

def cortar(entrada):
	cadena = entrada.replace("solve", "")
	cadena = cadena.replace("[", "").replace("]", "")
	cadena = cadena.replace(" ", "")
	return entrada

def operar(entrada):
	patron = '\/\d*\.?\d+|\*\d*\.?\d+|\-\d*\.?\d+|\+\d*\.?\d+|\d*\.?\d+|\w+[(][^)]+[)]|\+\w+[(][^)]+[)]|\-\w+[(][^)]+[)]|\*\w+[(][^)]+[)]|\/clea\w+[(][^)]+[)]'
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

def triangle(entrada):
	patron = '\d+'
	cadena = re.findall(patron, entrada)
	Metodos.triangleAsc(int(cadena[0]), 0)

def triangleDes(entrada):
	patron = '\d+'
	cadena = re.findall(patron, entrada)
	Metodos.triangleDes(int(cadena[0]))

def sort(entrada):
	patron = '\d*\.?\d+|\-\d*\.?\d+'
	cadena = re.findall(patron, entrada)
	lista = []
	for i in cadena:
		lista.append(float(i))
	Metodos.QuickSort((lista),0,len(lista) - 1)
	if 'asc' in entrada:
		print(lista)
	elif 'desc' in entrada:
		print(lista[::-1])
	else:
		print("Syntax Error")

def rombo(entrada):
	patron = '\d+'
	cadena = re.findall(patron, entrada)
	Metodos.rombo(int(cadena[0]))

def exec(entrada):
	patron = '["][^"]+["]'
	cadena = re.findall(patron, entrada)
	try:
		cadena = cadena[0].replace("\"", "")
		return cadena
	except :
		print("Syntax Error")

def documento(entrada):
	fic = open(entrada, "r")
	lines = []
	for line in fic:
		if line not in "\n":
   			lines.append(line)
	fic.close()

	for i in lines:
		
		scan(i)
		print("")
main()
