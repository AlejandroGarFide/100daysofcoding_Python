# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
wrd1 = ["t", "r", "u", "e"]
wrd2 = ["l", "o", "v", "e"]

contador_1 = 0
contador_2 = 0

n1_lwr = name1.lower()
n2_lwr = name2.lower()
names = n1_lwr + n2_lwr

for i in wrd1:
  contador_1 += names.count(i)

for i in wrd2:
  contador_2 += names.count(i)
score = str(contador_1) + str(contador_2)

if int(score) < 10 or int(score) > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif int(score) >= 40 and int(score) <= 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}")
