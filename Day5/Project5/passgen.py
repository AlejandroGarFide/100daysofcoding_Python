#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 
 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("¡Bienvenido al generador de contraseñas PyPass!")
nr_letters= int(input("¿Cuántas letras quieres en tu contraseña?\n")) 
nr_symbols = int(input(f"¿Cuántos símbolos quieres en tu contraseña?\n"))
nr_numbers = int(input(f"¿Cuántos números quieres en tu contraseña?\n"))

contrasena = []
for letra in range(1,nr_letters+1):
    contrasena.append(random.choice(letters))

for simbolo in range(1,nr_symbols+1):
    contrasena.append(random.choice(symbols))

for numeros in range(1,nr_numbers+1):
    contrasena.append(random.choice(numbers))

random.shuffle(contrasena)
print(''.join(contrasena))
