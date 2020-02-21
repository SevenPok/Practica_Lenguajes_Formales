import re
import Metodos



def scan(entrada):
	comando = str(entrada).lower()
	if 'solve' in comando:
		cadena = comando.replace("solve", "")
		cadena = cadena.replace("[", "").replace("]", "")
		cadena = cadena.replace(" ", "")
		operar(cadena)

def operar(entrada):
	patron = '\-\d*\.?\d+|\+\d*\.?\d+|\d*\.?\d+|\w+[(][^)]+[)]|\+\w+[(][^)]+[)]|\-\w+[(][^)]+[)]'
	cadena = re.findall(patron,entrada)
	print(cadena)
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
    
