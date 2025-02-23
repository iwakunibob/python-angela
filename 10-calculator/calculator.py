# Calculator Project by Robert Laurie
import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2
    
def divide(n1, n2):
    return n1 / n2

print(art.logo)
print("Welcome to the RPN Calculator Project")
operations = {'+':add, '-': subtract, '*':multiply, '/':divide}
loop = 'y'
accum = float(input("What is the first number? "))
while loop == 'y':
    number = float(input("What is the next number? "))
    op = input("What is the operation? + - * /? ")
    answer = operations[op](accum, number)
    print(f"Your result for {accum} {op} {number} = {answer}")
    loop = input("Use answer for next operation? Y or N \n").lower()
    if loop == 'y':
        accum = answer
