# asks what is the first number?
# the program will store what the user put in.
# asks what is the operand
# the program will store what the user put in.
# asks what is the second number?
# the program will store what the user put in.
# the program will take the three stored variables and write into equation. 


# ask the user for the inputted formula
print "Which math operation do you want to perform?"
print "Please enter operator ( + - * /) followed by two numbers"
user_input = raw_input("For example: + 1 2 \n ")
# find out the operation to perform
user_input[0] 
if user_input[0] == "*":
	print int(user_input[2]) * int(user_input[4])
elif user_input[0] == "/":
	print int(user_input[2]) / int(user_input[4])
elif user_input[0] == "+":
	print int(user_input[2]) + int(user_input[4])
elif user_input[0] == "-":
	print int(user_input[2]) - int(user_input[4])
else:
	print "Try again"

# display it to user
