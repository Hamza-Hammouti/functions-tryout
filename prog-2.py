def addition(number1, number2):
    total = number1 + number2
    return str(number1) + " + " + str(number2) + " = " + str(total)

def subtraction(number1, number2):
    total = number1 - number2
    return str(number1) + " - " + str(number2) + " = " + str(total)

def multiplication(number1, number2):
    total = number1 * number2
    return str(number1) + " x " + str(number2) + " = " + str(total)

def division(number1, number2):
    total = number1 / number2
    return str(number1) + " : " + str(number2) + " = " + str(total)

def increment(number):
    total = number + 1
    return str(number) + " + 1 = " + str(total)

def decrement(number):
    total = number - 1
    return str(number) + " - 1 = " + str(total)

print("----------------")
print(addition(20,20))
print(addition(10,20))
print(addition(20,15))
print("----------------")
print(subtraction(20,20))
print(subtraction(10,20))
print(subtraction(20,15))
print("----------------")
print(multiplication(20,20))
print(multiplication(10,20))
print(multiplication(20,15))
print("----------------")
print(division(20,20))
print(division(10,20))
print(division(20,15))
print("----------------")
print(increment(20))
print(increment(10))
print(increment(30))
print("----------------")
print(decrement(20))
print(decrement(10))
print(decrement(30))
print("----------------")