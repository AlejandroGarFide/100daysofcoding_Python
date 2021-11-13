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
index = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

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
print("Computer chose:\n", computer)

comb1 = ['Draw', 'You win', 'You lose']
comb2 = ['You lose', 'Draw', 'You win']
comb3 = ['You win', 'You lose', 'Draw']
matrix = [comb1, comb2, comb3]

print(matrix[ndx_computer][ndx_person])