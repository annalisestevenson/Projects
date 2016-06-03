tip_percentage = 18
bill_amount = 10

tip
def calculate_bill():
	return bill_amount + (bill_amount * 0.01 * tip_percentage)

def main():
	global bill_amount
	bill_amount = float(raw_input("How much is the bill not including tip?"))

	dine_alone = raw_input("Did you dine alone? Y/N")
	if dine_alone.upper() == "N":
		number_of_people = int(raw_input("How many people were at dinner?"))
		tip_percentage = (raw_input("Is 18 percent tip ok? Y/N"))
		if tip_percentage.upper() == "N":
			float(raw_input("How much do you want to leave for tip?"))
			print "Your total is" , calculate_bill/number_of_people
		else:
			print "Your total is" , calculate_bill/number_of_people
	else:
		tip_percentage = raw_input("Is 18 Y/N")
		if tip_percentage == "N":
			float(raw_input("How much do you want to leave for tip?"))
			
