from art import logo
from replit import clear

# Calculator Functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Operation Dictionary
operators = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

# Primary Program Loop
def calculator():
    print(logo)

    newCalc = True
    
    n1 = float(input('First number: '))

    while newCalc == True:
        print('Select Operation.')
        for symbol in operators:
            print(symbol)
        opp = input('Selected operation: ')

        n2 = float(input('Second number: '))

        function = operators[opp]
        answer = function(n1, n2)

        print(f'\n{n1} {opp} {n2} \nans = {answer}\n')
        n1 = answer

        usrContinue = input('New operation on ans? (y/n): ').lower()
        if usrContinue == 'n' or usrContinue == 'no':
            newCalc = False
            clear()
            usrExit = input('Quit calculator? (y/n): ').lower()
            if usrExit == 'y' or usrExit == 'yes':
                exit = True
                print('Goodbye!')

quit = False
while quit == False:
    calculator()
    quit = exit


