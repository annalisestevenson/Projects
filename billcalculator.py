bill_amount = 10
def tip_amount(tip_percentage):
	return bill_amount * tip_percentage * 0.01
# print tip_amount(10, 15)
def total_bill(tip_amount):
	return tip_amount + bill_amount
# print total_bill(1.5, 10)
def bill_split(number_people):
	return bill_amount / number_people
print bill_split(2)
# def main():
# answer = raw_input("Pick a number: 1- Calculate Tip, 2- Split the bill")
# if answer == 1:
# 	print tip_amount(15)
# 	print total_bill(tip_amount)
# bill_split1 = raw_input("Would you like to split the bill? Y/N")
# # print main()
# if bill_split1 == "Y":
# 	number_people1 = int(raw_input("How many people?"))
# 	print bill_split(number_people1)
# if answer == 2:
# 	print bill_split(number_people)
