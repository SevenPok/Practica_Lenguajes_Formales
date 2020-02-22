
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def ackermann(n, m):
    if n == 0:
        return m + 1
    elif m == 0:
        return ackermann(n - 1,1)
    else:
        return ackermann(n - 1, ackermann(n, m - 1))



def exponente(n,m):
    if m == 0:
        return 1
    elif m == 1:
        return n
    else:
        return n * exponente(n,m-1)

def suma(n):
   if len(n) == 1:
        return n[0]
   else:
        return n[0] + suma(n[1:])

def QuickSort(numeros, izq, der):

    pivote = numeros[izq]
    i = izq
    j = der
    aux = 0

    while i < j:
        while numeros[i] <= pivote and i < j:
            i += 1

        while numeros[j] > pivote:
            j -= 1

        if i < j:
            aux = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = aux

    numeros[izq] = numeros[j]
    numeros[j] = pivote

    if izq < j-1:
        QuickSort(numeros,izq,j-1)

    if j+1 < der:
        QuickSort(numeros,j+1,der)

def triangleDes(n):
    if n < 0:
        return 
    else:
        for i in range(0,n):
            print("*",end="")
        print("")
        triangleDes(n-1)

def triangleAsc(n, inicio):
    if n < 0:
        return
    else:
        for i in range(0,inicio):
            print("*",end="")
        print("")
        triangleAsc(n-1,inicio+1)

def piramide(n, inicio):
    if n == 0:
        return
    else:
        for i in range(0,n):
            print(" ",end="")
        
        for i in range(0,inicio*2+1):
            print("*",end="")
        print("")
        piramide(n-1,inicio+1)

def piramideInv(n,inicio):
    if n < 0:
        return
    else:
        for i in range(0,inicio):
            print(" ",end="")

        for i in range(0,n*2+1):
            print("*",end="")
        print("")
        piramideInv(n-1,inicio+1)

def rombo(n):
    if n > 0:
        piramide(n,0)
        piramideInv(n,0)

