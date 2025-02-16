"""
Program: average_scores.py
Author: Patrick Foy
Last date modified: 2/8/2025

The purpose of this program is to get input values and output them with average score.

1/24/2025 - Program created.

2/8/25 - I reworked this from previous to include validation for grades entered, added a constant for number of grades,
added a while loop for the input to eliminate excess duplicate code. Also added additional comments.
"""

#variables
count_cycle = 0
score_total = 0.00
input_score = 0.00
average_score = 0.00

#inputs 
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
number_scores = int(input("Enter How many scores you want to average: "))

while count_cycle != number_scores: # will continue to run while countCycle is not equal to NUMBER_SCORES
    
    try :
        input_score = float(input('Enter Your Score out of 100: ')) # takes string converts to float and stores it to input_score
        score_total += input_score #takes input_score plus any previous score and places sum in score_total variable 
        count_cycle = count_cycle + 1 # increases sum of count_cycle by 1 for each entry
    except :
        print ("An exception has occurred please make sure value is a number not line of text") #if anything other than an int or a float is entered in the input statement this will trigger

#calculation of average score
average_score = score_total / number_scores

#output with formatting
print("{ln}, {fn} age: {a} average grade: {finalScore:0.2f}".format(finalScore = average_score, a=age, ln=last_name, fn=first_name))

#Test 1
#Enter your first name: Patrick
#Enter your last name: Foy
#Enter your age: 37
#Enter Your Score out of 100: 85.5
#Enter Your Score out of 100: 95
#Enter Your Score out of 100: 87.3
#Foy, Patrick age 37 average grade: 89.27

#test 2
#Enter your first name: John
#Enter your last name: Doe
#Enter your age: 100
#Enter Your Score out of 100: 67.3
#Enter Your Score out of 100: 57.5
#Enter Your Score out of 100: 47.33
#Doe, John age: 100 average grade: 57.38


#Test 3
#Enter your first name: Jane
#Enter your last name: Doe
#Enter your age: 25
#Enter Your Score out of 100: 25.3333333
#Enter Your Score out of 100: 87.666666
#Enter Your Score out of 100: 0
#Doe, Jane age: 25 average grade: 37.67