# BMI Program by Robert Laurie

print("Welcome to the BMI Body Mass Index program")
height = int(input("What is your height in cm? "))
weight = int(input("What is your weight in kg? "))

bmi = weight / (height / 100) ** 2
print(round(bmi, 2))  # round float 2 decimal places
print(f"Your score is = {round(bmi,2)}\nFor height = {height}\nand weight = {weight}")
if bmi <= 18.5:
    print("You are under-weight")
elif bmi < 25:
    print("You are normal-weight")
else:
    print("You are over-weight")
