"""
1. Ejercicio: Dado un número, imprime si es positivo o negativo.
2. Ejercicio: Dado un número, imprime si es par o impar.
3. Ejercicio: Dado tres números, encuentra y muestra el mayor de ellos.
"""
numero=9
if numero>0:
    print ('positivo')
else:
    print('negativo')

if numero % 2 == 0:
    print ('par')
else:
    print ('impar')

a,b,c = 1, 25, 50
mayor = max(a,b,c)
print (mayor)
