"""
Name: Maher Ibrahim
Class: Fall - INSY-3300
Homework 1: Homework #1
Date: 09/13/2019
Description: This program will ask the user to input an integer and display what day of the week it is.
"""
#asks user to type a number 1 - 7
Userinput=int(input("pick a number between 1 and 7: "))
#if and elif statments
if Userinput==1:
    print("It is Monday ")
elif Userinput==2:
    print("It is Tuesday ")
elif Userinput==3:
    print("It is Wednesday ")
elif Userinput==4:
    print("It is Thursday ")
elif Userinput==5:
    print("It is Friday ")
elif Userinput==6:
    print("It Is Saturday")
elif Userinput==7:
    print("It is Sunday")
elif int(Userinput>7):
    print("Error! Number Greater Than 7 Try Again! ")
elif int(Userinput<1):   
    print("Error! Number smaller than 1 Try Again! ")


