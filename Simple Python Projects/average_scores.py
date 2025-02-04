"""
Program: average_scores.py
Author: Patrick Foy
Last date modified: 01/24/2024

 

The purpose of this program is to get input values and out put them with average score
"""

firstname = input("Enter your first name: ")

lastname = input("Enter your last name: ")

age = input("Enter your age: ")

input_score = input('Enter Your First Score out of 100: ')

convert_score1 = float(input_score)

input_score = input('Enter Your Second Score out of 100: ')

convert_score2 = float(input_score)

input_score = input('Enter Your Third Score out of 100: ')

convert_score3 = float(input_score)

score_total = convert_score1+convert_score2+convert_score3

average_score = score_total/3

print("{ln}, {fn} age: {a} average grade: {finalscore:0.2f}".format(finalscore= average_score, a=age, ln=lastname, fn=firstname))


#Test 1
#Enter your first name: Patrick
#Enter your last name: Foy
#Enter your age: 37
#Enter Your First Score out of 100: 85.5
#Enter Your Second Score out of 100: 95
#Enter Your Third Score out of 100: 87.3
#Foy, Patrick age 37 average grade: 89.27

#test 2
#Enter your first name: John
#Enter your last name: Doe
#Enter your age: 100
#Enter Your First Score out of 100: 67.3
#Enter Your Second Score out of 100: 57.5
#Enter Your Third Score out of 100: 47.33
#Doe, John age: 100 average grade: 57.38


#Test 3
#Enter your first name: Jane
#Enter your last name: Doe
#Enter your age: 25
#Enter Your First Score out of 100: 25.3333333
#Enter Your Second Score out of 100: 87.666666
#Enter Your Third Score out of 100: 0
#Doe, Jane age: 25 average grade: 37.67