# day = raw_input("What day is it?")
# def alarm_clock(day, vacation):
	# today = day.lower
	# Sunday = int(0)
	# Monday = int(1)
	# Tuesday = int(2)
	# Wednesday = int(3)
	# Thursday = int(4)
	# Friday = int(5)
	# Saturday = str(s)
	# Sunday = str(s)
	# vacation = True or False

	# if today >= 1 and today <= 6:
		 # return alarm_clock("7:00", off)
	# print alarm_clock

def alarm_clock(day, vacation):
	if vacation == True:
		return "Off"
	if day > 0  and day < 6 and day != 's':
		return '7:00'
	elif day == 0  or day == 6 or day == 's':
		return '10:00'
	else:
		return "Off"

# my_day = raw_input("What day is it? (0-6)")
# my_vacation = raw_input("Are you on vacation? (T/F)")
# print alarm_clock(my_day, my_vacation)
#Tues, not on vacation
print alarm_clock(2, False)
# Sun, on vacation
print alarm_clock(0, True)
#Fri, not on vacation
print alarm_clock(5, False)