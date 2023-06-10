from art import logo
import os
clear = lambda: os.system('cls')

def add(firstNum, secondNum):
    answer = firstNum + secondNum
    return answer

def subtract(firstNum, secondNum):
    answer = firstNum - secondNum
    return answer

def multiply(firstNum, secondNum):
    answer = firstNum * secondNum
    return answer

def divide(firstNum, secondNum):
    answer = firstNum / secondNum
    return answer

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    firstNum = float(input("What's the first number?: "))
    for key in operations:
        print(key)

    calc_running = True

    while calc_running:
        operator = input("Pick an operation: ")
        secondNum = float(input("What's the next number?: "))
        
        answer = operations[operator](firstNum, secondNum)
        print(f"{firstNum} {operator} {secondNum} = {answer}")

        moreCalc = input(f"Type 'y' to continue calculating with {answer}, or type "\
            "'n' to start a new calculation: ")

        if moreCalc == 'y':
            firstNum = answer
        else:
            clear()
            calculator()

calculator()