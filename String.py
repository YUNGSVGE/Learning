#Example 1 User inputs name
# name = ""
#user = input(f"Enter Your Name! \n {name}")
#print(name)


#Example 2 prints the H as an array of characters 
#print (a[0])


#Example 3 lower cases text
name = "SVGE"
name = name.lower()
print(name)

#Example 4 upper cases text
name = "SVGE"
name = name.upper()
print(name)

#Example 5 Splits text by making it into an array
name = "SV,GE"
name = name.split(",")
print(name)

#Example 6 creates a boolean true/false to check if the word "the" exists
name = "I live the space ship"
does = name.__contains__("the")
print(does)

#Example 6 creates a boolean true/false to check if the word "the" exists
if "the" in name:
    print(does)
