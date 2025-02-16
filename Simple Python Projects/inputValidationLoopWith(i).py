'''
Program: input_while.py
Author: Patrick Foy
Last date modified: 2/11/2025

The purpose of this program is to get input value for times 
to run the list process get values within a range and add them
to the list for the number of iterations that the user input. Finally
it out puts the list. This uses a iteration variable.
'''

varList = []
userStop = int(input("Enter a number of times to run the program: "))
i = 0

while i != userStop:
    userInput = int(input("Enter a number: "))
    while userInput > 100 or userInput < 1:
        userInput = int(input("Enter a valid Number: ")) 
    varList.append(userInput)
    i = i + 1
    for x in varList:
        print(x)