def calculate_tip(bill_amount, tip_percentage):
	return bill_amount * tip_percentage * .01

def calculate_bill_total(tip, bill_amount):
	return bill_amount + tip

def split_bill(bill_amount, number_people):
	return bill_amount / number_people

def main():
	print "Please choose one of the following"
	print "1- Calculate Tip"
	print "2- Split Bill"
	choice = int(raw_input())

	if choice == 1:
		bill = float(raw_input("How much was your bill?"))
		tip_percentage = float(raw_input("How much do you want to tip?"))
		tip = calculate_tip(bill, tip_percentage)
		bill_total = calculate_bill_total(tip, bill)
		print "The tip is %f." % tip
		print "The bill total is %f." % bill_total
		is_split = raw_input("Would you like to split the bill? Y/N")
		if (is_split.upper() == "Y"):
			split_number = int(raw_input("How many people?"))
			split_amount = split_bill(bill_total, split_number)
			print "The bill is %f for each person." % (split_amount)
	elif choice == 2:
		bill = float(raw_input("How much was your bill?"))
		split_number = int(raw_input("How many people?"))
		split_amount = split_bill(bill, split_number)
		print "The bill is %f for each person." % (split_amount)

if __name__ == '__main__':
	main()