rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
index = int(input("¿Qué eliges? Escribe 1 para Piedra, 2 por Papel o 3 por Tijeras.\n"))-1

if index >= 3 or index < 0:
  print('El número que introdujiste es inválido. Perdiste.')
else:
  print("Elegiste:")
  options = [rock, paper, scissors]
  computer = random.choice(options)
  person = options[index]

  ndx_person = index
  ndx_computer =  0

  if computer == rock:
    ndx_computer = 0
  elif computer == paper:
    ndx_computer = 1
  else:
    ndx_computer = 2

  print(options[index])
  print("La computadora eligió:\n", computer)

  comb1 = ['Empate', 'Ganaste', 'Perdiste']
  comb2 = ['Perdiste', 'Empate', 'Ganaste']
  comb3 = ['Ganaste', 'Perdiste', 'Empate']
  matrix = [comb1, comb2, comb3]

  print(matrix[ndx_computer][ndx_person] + '.')