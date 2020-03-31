"""
Name: Maher Ibrahim
Class: Fall - INSY-3300
Homework 1: Homework #2
Date: 09/13/2019
Description: This program will ask the user to input an integer and display if they're a Adult, Teenager, Child or infant.
"""
# asks user to input age
age = int(input("Enter your age 1 - 100 "))
# if statement
if age >= 20:
    print("You're an Adult")
elif age >= 13:
    print("You're a Teenager")
elif age > 1:
    print("You're a Child")
else:
    print("You're an Infant")