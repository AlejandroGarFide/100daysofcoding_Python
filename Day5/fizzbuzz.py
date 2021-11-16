"""
En este ejercicio, se corre un juego de lógica en el que, al contar del 1 al 100, 
por cada número divisible entre 3, se imprime la palabra "Fizz" y si es divisible
entre 5, la palabra es "Buzz", peeero, si es divisible por ambos (3 y 5), entonces
se imprime la palabra "FizzBuzz". Este es parte de los ejercicios para el reto del 
día 5.
"""

for numero in range(1,31):
    if numero % (3*5) == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)
