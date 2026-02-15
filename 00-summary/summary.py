# This is my Python3 notes by Robert Laurie
# Last updated 2026
# VSCode setup https://www.youtube.com/watch?v=D2cwvpJSBX4
print("Hello Earth") 
# Variables use typically use snake_case
first_name = "Robert"  # String data type in " "
age = 68  # Integer data type
degF = 98.6  # Float data type
citizen = True # Boolean data type True/False
print(f"{first_name}'s age={age}\nTemp={degF}F Citizen: {citizen}")
# Only 4 data types exist in python  and can be converted expliitly
print(float(age))
print("Age = " + str(age))
print("Temp = " + str(int(degF)))
print(bool(""))
print(bool(0.0))
print(bool("abc"))
print(bool(2))
""" Muliline comment start
Operators are evaluated in a specific order:
** (Exponentiation)
~, +, - (Bitwise NOT, unary plus, unary minus)
*, /, //, % (Multiplication, division, floor division, modulo)
+, - (Addition, subtraction)
<<, >> (Left and right bitwise shifts)
& (Bitwise AND)
^ (Bitwise XOR)
| (Bitwise OR)
==, !=, <, <=, >, >=, is, is not, in, not in (Comparisons, identity, membership)
not (Logical NOT)
and (Logical AND)
or (Logical OR)
:= (Walrus operator)
Muliline comment end """ 
# n1 = int(input("First Number = "))
# n2 = int(input("Second Number = "))
# # fString can be used to mix types in print or store in variable
# display =  f"{n1}+{n2}={n1+n2}\n{n1}-{n2}={n1-n2}\n"
# display += f"{n1}*{n2}={n1*n2}\n{n1}/{n2}={n1/n2}\n"
# display += f"{n1}//{n2}={n1//n2}\n{n1}%{n2}={n1%n2}\n"
# display += f"{n1}**{n2}={n1**n2}\n{n2}**{n1}={n2**n1}\n"
# print(display)

# BMI Program by Robert Laurie
# print("Welcome to the BMI Body Mass Index program")
# height = int(input("What is your height in cm? "))
# weight = int(input("What is your weight in kg? "))
# bmi = weight / (height / 100) ** 2
# print(round(bmi, 2))  # round float 2 decimal places
# print(f"Your score is = {round(bmi,2)}\nFor height = {height}\nand weight = {weight}")
# if bmi <= 18.5:
#     print("You are under-weight")
# elif bmi < 25:
#     print("You are normal-weight")
# else:
#     print("You are over-weight")

# While Loops
i = 1
while i < 6:
    print(i, end=", ")
    i += 1
print("\b\b \nDone")

# for range  first, last, incr
for x in range(0, 20, 4):
    print(x, end=", ")
print("\b\b \nDone")
for y in range(5, 10):
    print(y, end=", ")
print("\b\b \nDone")
for z in range(10):
    print(z, end=", ")
print("\b\b \nDone")

# Python Lists can contain a mix of data types or just one
demolist = ["abc", 34, True, 40, "male"]
print(demolist)
print(demolist[4])
demolist[0] = "cars"
demolist[2:4] = ["vw", "bmw"] # Change Slices 2 and 3
print(demolist)
demolist.append("ford") # append item to end
demolist.remove("male") # remove item by data
demolist.pop(1)  # delete item by index
print(demolist)
for item in demolist:
    print(item, end=", ")
print("\b\b \nDone")
[print(item, end=", ") for item in demolist]
print("\b\b \nDone")
demolist.sort()
print(demolist)
demolist.remove("cars")
demolist.append("buick")
demolist.sort(reverse=True)
print(demolist)
demolist.clear()
print(demolist)
