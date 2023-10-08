"""
Crea una función para verificar si un número es par o impar y devuelva “El número es par” o “El número es impar” según corresponda.
"""
numero=8
def es_par(numero): 
    return numero % 2 == 0 
if es_par(numero):
    print("Es un número par.") 
else: 
    print("Es un número impar.")

"""
Crea una función a la que pases un número como argumento, calcule el factorial de ese número y haga print del resultado.
"""
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(3))

"""
Crea una función a la que se le pase un número como argumento, calcule la cantidad de dígitos y haga print de “La cantidad de dígitos es:” y el resultado total de dígitos.
"""
numero2=616
def contar_digitos(numero2): 
    return len(str(numero2)) 
print("La cantidad de dígitos es:", contar_digitos(numero2))

"""
 Dada una lista de números, crea una función que devuelva el número máximo de la lista.
"""
lista = [120,150,5]
def encontrar_maximo(lista): 
    maximo = lista[0] 
    for numero in lista: 
        if numero > maximo: 
            maximo = numero 
            return maximo  
print("El número máximo es:", encontrar_maximo(lista))

"""
Crea una función que, dado un número, sume los dígitos de ese número y devuelva el resultado.
"""
numero3=89
def sumar_digitos(numero3): 
    suma = 0 
    while numero3 > 0: 
        suma += numero3 % 10 
        numero3 //= 10
    return suma + numero3 
print("La suma de los dígitos es:", sumar_digitos(numero3))

""""
Dados dos números, crea una función para encontrar el mínimo común múltiplo (MCM) de los dos números, que se les pasarán como argumento a la función, y
devuelva el MCM.
"""
numero4=3
numero5=7
def mcm (numero4, numero5):
    if numero4 == 0 or numero5 == 0: 
        return 0 
    else: 
        maximo = max(numero4, numero5) 
        while True: 
            if maximo % numero4 == 0 and maximo % numero5 == 0: 
                return maximo 
            maximo += 1 
print("El MCM es:", mcm(numero4, numero5))

""""
Crea una función a la que, pasándole la base y la altura, calcule y devuelva el área de un triángulo.
"""
base=3
altura=7
def area_triangulo(base, altura): 
    return (base * altura) / 2 
print("El área del triángulo es:", area_triangulo(base, altura))

"""
 Crea una función que, dado un número, verifique si un número es positivo, negativo o cero.
 """
def tipo_numero(numero6):
    if numero6 > 0:
        return "El número es positivo"
    elif numero6 < 0:
        return "El número es negativo"
    else:
        return "El número es igual a 0"
numero6 = float(input("Ingresa un número: "))
print (tipo_numero(numero6))

"""
Crea una función que, dada una palabra, cuente la cantidad de letras en una palabra.
"""

def contador_letras (palabra):
    return (len(palabra))
palabra=str(input("Ingresa una palabra: "))
print (contador_letras(palabra))

"""Crea una función que, dado un número, verifique si un número es primo.
"""

def numero_primo(numero7):
    if numero7 <=1:
        return "El número no es primo"
    for i in range (2, numero7):
        if numero7 % i == 0: 
            return "El número no es primo"
        else:
            return "El número es primo"
numero7=int(input("Ingresa un número: "))
print (numero_primo(numero7))