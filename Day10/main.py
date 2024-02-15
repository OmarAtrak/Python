from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number: "))
num2 = int(input("What's the second number: "))
operation = input("Type operation '+' , '-' , '*' , '/'\n")
result = operations[operation](num1, num2)

isProgramStop = False
stopProgram = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit: ")

if stopProgram.lower() == 'n':
    isProgramStop = True

while not isProgramStop:
    operation = input("Type operation '+' , '-' , '*' , '/'\n")
    num1 = result
    num3 = int(input("What's the second number: "))
    result = operations[operation](num1, num3)
    print(f"{num1} {operation} {num3} = {result}")

    stopProgram = input("Type 'y' to continue calculating with 8, or type 'n' to exit: ")
    if stopProgram.lower() == 'n':
        isProgramStop = True
