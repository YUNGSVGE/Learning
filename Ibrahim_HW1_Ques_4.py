
"""
Name: Maher Ibrahim
Class: Fall - INSY-3300
Homework 1: Homework #4
Date: 09/13/2019
Description: This program will ask the user to input the temp and will output a table zero through thirty two
"""
#Displays Promt to User
print(" Celsius to Fahrenheit Table ")
print("C       F")
# Loop 
for C in range(0,21):
    #Math Formula
    F=(9/5)*C+32
    #Prints Celsius with Fahrenheit
    print(C,"    {0:.2f}".format(F))