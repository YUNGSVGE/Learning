#Int Var
logAttempt = 3
LogMax = 5

#pizzaTime = 1 True, pizzaTime = 0 False, pizzaTime = True, pizzaTime = False

#Password Authentication True/False Example
passwordTyped = "PASSWORD"
actualPassword = "PASSWORD"

#Checks if password type is the same as actual password then checks if amount of login attemps are less than login maximum
pizzaTime = (passwordTyped == actualPassword) or (logAttempt < LogMax)

#Prints if true or false
print(pizzaTime)



