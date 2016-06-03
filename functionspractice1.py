# def add(num1, num2):
# 	return num1 + num2
# print add(4,5)


# def subtract(num1, num2):
# 	return num1 - num2
# print subtract(4,2)

# def multiply(num1, num2):
# 	return num1 * num2
# print multiply(4, 5)

# def divide(num1, num2):
# 	return num1 / num2
# print divide(10, 2)

# def modulo(num1, num2):
# 	return num1 % num2
# print modulo(3,2)

# def power(base, exponent):
# 	return base ** exponent
# print power(2,5)

# def square(num):
# 	return num ** 2
# print square(2)

# def smalladd(num1, num2):
# 	return num1 + num2
# smalladd(4, 5)
# big1 = 9

# def smallsubtract(num1, num2):
# 	return num1 - num2
# smallsubtract(9, 6)
# big2 = 3

# total = big1 + big2
# print total

# print add(add(4, 5), subtract(9, 6))


def add(num1, num2):
	return num1 + num2
def subtract(num1, num2):
	return num1 - num2
def multiply(num1, num2):
	return num1 * num2
def divide(num1, num2):
	return num1 / num2
def modulo(num1, num2):
	return num1 % num2
def power(num1, num2):
	return num1 ** num2
def square(num1):
	return power(num1, 2)
#8a --> (4+5) + (9-6)
# a = add(4, 5)
# b = subtract(9, 6)
# print add(a, b)

# OR ANOTHER WAY IS TO PUT IT ALL ON 1 LINE

# print add(add(4, 5), subtract(9, 6))
 # 8e
 # (3%4) / 9*9
# a = modulo(3,4)
# b = multiply(9, 9)
# print divide(a, b)

# or another way
# print divide(modulo(3,4), multiply(9,9))


# 8h
# 3^(2+3)
# a= add(2, 3)
# b = power(3, a)
# print b

# 8 b
# print subtract(divide(12, 2), 60)

# OR
# a = divide(12, 2)
# b = 60
# print subtract(a, b)

# 8c
# a = add(1, 2)
# b = 3
# print add(a, b)

# 8d
# a = add(1, 2)
# print square(a)

# 8f
# a = 7
# b = add(3, 8)
# print multiply(a, b)

# 8g
# a = add(1, 2)
# b = add(4, 5)
# c = multiply(3, b)
# d = subtract(a, c)
# print d

# 8h
a = 3
b = add(2, 3)
print power(a, b)



