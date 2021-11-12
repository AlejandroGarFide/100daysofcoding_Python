# 🚨 Don't change the code below 👇
age = input("What is your current age?\n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
days = (365 * 90) - int(age) * 365
weeks = (52 * 90) - int(age) * 52
months = (12 * 90) - int (age) * 12

#Another solution
years_remaining = 90 - int(age)
days_left = years_remaining * 365
weeks_left = years_remaining * 52
months_left = years_remaining * 12

print(f"You have {days_left} days, {weeks_left} weeks and {months_left} months left")
