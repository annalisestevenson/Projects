global_bill_amount = int(raw_input("What is the bill amount?"))
tip_amount = 0

def calculate_tip():
	tip_percentage = float(raw_input("How much do you want to tip?"))
	return global_bill_amount * tip_percentage


def calculate_total_bill():
	global global_bill_amount
	global_bill_amount + tip_amount
	return global_bill_amount

def split_bill(number_of_people):
	number_of_people = int(raw_input("How many people are there?"))
	return global_bill_amount / number_of_people

tip_amount = calculate_tip()

print "Your tip amount is" , tip_amount
print "Total Bill is" , calculate_total_bill()
bill_per_person = split_bill()
print "Amount per person is" , bill_per_person