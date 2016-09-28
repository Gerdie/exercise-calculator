def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def square(num1):
    return num1 * num1

def cube(num1):
    return num1 * num1 * num1

def power(num1, num2):
	base = num1
	if num2 == 0:
		return 1
	elif num2 < 0:
		base = 1/num1
		num2 = abs(num2)
	for i in range(num2 - 1):
		num1 *= base
	return num1

def mod(num1, num2):
    return num1 % num2
