import random
from hangman_art import logo
from hangman_art import stages
from words_hangman import word_list
from replit import clear 

print(logo)
print('¡Bienvenido al juego del ahorcado!\n')
print("Nomás te advierto que las palabras están en inglés.")

palabra = random.choice(word_list)
display = []
vidas = 6
porras = ["¡Bien hecho!", "Sigue así", "¡Súper!", "Lo haces bien. :)"]


for i in range(len(palabra)):
    display.append('_')

while vidas > 0 and '_' in display:
    intento = input('\nIntroduce una letra cualquiera:\n').lower()

    clear()

    for indice in range(len(palabra)):
        letra = palabra[indice]
        if letra == intento:
            display[indice] = intento
    
    print(f"\n{' '.join(display)}\n")
    
    if intento in palabra:
        print(random.choice(porras)) 
    else:
        vidas -= 1
        print(f"Error. Te quedan {vidas}, vidas.")

    if vidas == 0:
        print("Perdiste")
    elif '_' not in display:
        print("¡Felicidades, Shinji! ¡Ganaste!")

    print(stages[vidas])

if vidas == 0:
    print(f"La palabra que estabas buscando fue: {palabra}\n\n\n")