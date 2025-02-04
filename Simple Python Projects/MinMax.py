"""
Program: MinMax.py
Author: Patrick Foy
Last date modified: 01/28/2024

 

The purpose of this program is to take two floats and compare them to two constants.
"""
MAX = 10
MIN = 0

print("Please Enter a number for Y")
input_item = input()
Y = float(input_item)
if Y > MAX:
    print("Y is Greater than 10")
else:
    print("Y is not Greater than 10")

if Y < MIN:
    print("Y is Below 0")
else:
    print("Y is not Below 0")

print("Please Enter a new number for X")
input_item = input()
X = float(input_item)

if MIN < X < MAX and MIN != X and X != MAX:
    print("X is between 0 and 10 and does not equal 10 nor 0.")
else:
    print("X is not between 0 and 10 and does not equal 10 nor 0.")
    
if MIN < X < MAX and MIN != X:
    print("X is within 0 and up to 10 but is not equal 10")
else:
    print("X is not within 0 and 10 or does equal 10")
    15
if MIN < X <= MAX:
    print("X is above 0 up to and including 10")
else:
    print("X is either not above 0 or exceeds 10")