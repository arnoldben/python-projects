from art import logo

print("\nWelcome to LTO Car Registration Renewal Schedule\n")
print(logo)
plate_number = input("Enter your car's plate number: ")
last_digit = plate_number[-1]
second_to_last_digit = plate_number[-2]

MONTHLY_SCHED = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
]

month = MONTHLY_SCHED[int(last_digit) - 1]

WEEKLY_DEADLINE = [
    "1st week of " + month + " (1 to 7)",
    "2nd week of " + month + " (8 to 14)",
    "3rd week of " + month + " (15 to 21)",
    "4th week of " + month + " (22 up to the last day of the month)",
]

if 1 <= int(second_to_last_digit) <= 3:
    print("Vehicle Registration Renewal Schedule: " + WEEKLY_DEADLINE[0] + "\n")
elif 4 <= int(second_to_last_digit) <= 6:
    print("Vehicle Registration Renewal Schedule: " + WEEKLY_DEADLINE[1] + "\n")
elif 7 <= int(second_to_last_digit) <= 8:
    print("Vehicle Registration Renewal Schedule: " + WEEKLY_DEADLINE[2] + "\n")
elif 9 <= int(second_to_last_digit) <= 0:
    print("Vehicle Registration Renewal Schedule: " + WEEKLY_DEADLINE[3] + "\n")
