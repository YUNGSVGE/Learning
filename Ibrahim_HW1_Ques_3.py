
"""
Name: Maher Ibrahim
Class: Fall - INSY-3300
Homework 1: Homework #3
Date: 09/13/2019
Description: This program will ask the user to input the quanity and output the amount of discount
"""
#Declaring Varibles of the discounts
Discount10 = .1
Discount20 = .2
Discount30 = .3
Discount40 = .4
#Asking user to input the amount of quantity they are going to purchase 
quantity = int(input("What is the Quantity You want to buy? "))
#arithmetic equation
total = quantity * 99
#If & Elif statments
if quantity in range (1, 9):
    print(" No Discount applied, The Final Price is $:",total)
elif quantity in range (10, 19):
    print("Your Discount is $:",total*Discount10,"And The Final Price is $:",total-(total*Discount10))
elif quantity in range (20, 49):
    print("Your Discount is $:",total*Discount20,"The Final Price is $:",total-(total*Discount20))
elif quantity in range (50, 99):
    print("Your Discount is $:",total*Discount30,"The Final Price is $:",total-(total*Discount30))
elif quantity >=100:
    print("Your Discount is $:",total*Discount40,"The Final Price is $:",total-(total*Discount40))