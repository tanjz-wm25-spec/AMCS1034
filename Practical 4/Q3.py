HOURLY_RATE = 40
OT_REGULAR_RATE = HOURLY_RATE * 1.5
OT_EXCESS_RATE = HOURLY_RATE * 2
HOURLY_RATE_LIMIT = 35
REGULAR_RATE_LIMIT = 25

# Read working hour from the user
hours = float(input("Enter working hours: ")) 

if hours <= 35:
    regular_pay = hours * HOURLY_RATE
else:
    regular_pay = HOURLY_RATE_LIMIT * HOURLY_RATE
    hours -= HOURLY_RATE_LIMIT

if hours <= 25:
    overtime_pay = hours * OT_REGULAR_RATE
else:
    overtime_pay = REGULAR_RATE_LIMIT * OT_REGULAR_RATE
    hours -= REGULAR_RATE_LIMIT

overtime_pay += hours * OT_EXCESS_RATE

print("\n{:15s}: RM{:.2f}".format("Total salary", regular_pay + overtime_pay))
print("{:15s}: RM{:.2f}".format("-> Regular pay", regular_pay))
print("{:15s}: RM{:.2f}".format("-> Overtime pay", overtime_pay))