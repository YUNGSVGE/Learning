"""
Name: Maher Ibrahim
Class: Fall - INSY-3300
Homework 1: Homework #5
Date: 09/13/2019
Description: This program will ask the user to input the integer and will output the factorial 
"""

#asks user to input integer
userInt = int ( input("ENTER A INTEGER: "))
#validation check
while userInt <1:
  userInt = int(input("ERROR: ENTER A POSTIVE INTEGER!!!"))
  # for loop
fact = 1 
for firstNumber in range (1, userInt +1):
  fact = fact * firstNumber
  #prints the answer 
print()
print("THE FACTORIAL OF THE NUMBER", userInt, "IS", fact )