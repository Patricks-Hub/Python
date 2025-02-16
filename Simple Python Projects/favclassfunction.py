"""
Program: favclassfunction.py
Author: Patrick Foy
Last date modified: 2/8/2025

The purpose of this program is to get input for favorite subject and a number between 2 and 7
and output the favorite subject that many times using a function.
:param subject, a string containing the favorite subject
:param number, a integer between 2 and 7
:returns the subject with a space added the number of times user entered
"""
def multiply_string (subject, number):
    '''multiplies the string with space by the number of times and saves it to a variable'''
    subject_list = (subject + " ") * number
    ''':returns the subject with a space added the number of times user entered'''
    return subject_list
    
if __name__ == '__main__':
    ''':param subject, a string containing the favorite subject'''
    subject = input("Enter your favorite class: ")
    try:
        ''':param number, a integer between 2 and 7'''
        number = int(input("Enter a number between 2 and 7: "))
    except:
        print("You did not enter a number!!")
    else:
        '''checks that the entered number is between range of 2 and 7'''
        if number > 2 and number< 7:
            ''''prints function that writes the string subject the number of times entered'''
            print(multiply_string(subject,number))
        else:
            print("You must pick a number between 2 and 7")
            