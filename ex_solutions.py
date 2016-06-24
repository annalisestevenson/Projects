# def max(num1, num2):
# 	if num1> num2:
# 		return num1
# 	elif num1== num2:
# 		return "they are equal"
# 	else:
# 		return num2
# print max(2,4)

# def max_of_three(num1, num2, num3):
# 	return max(num1, num2, num3)
# print max_of_three(2, 4, 6)

# def min_of_three(num1, num2, num3):
# 	return min(num1, num2, num3)
# print min_of_three(2, 4, 6)

# def length_word(word):
# 	return len(word)
# print length_word("Carolyn")
	
# def character(letter):
# 	if letter== "a" or letter== "e" or letter== "i" or letter== "o" or letter== "u":
# 		return "True"
# 	else:
# 		return "False"
# print character("b")

# def prime(number):
# 	for n in range (2, number):
# 		if number % n==0:
# 			return False
# 	return True
# print prime(5)

luggage = int(raw_input("How much does your suitcase weigh?"))
if luggage>50:
	print "There is a $25 charge for your luggage"
else:
	print "Your luggage is free of charge"
