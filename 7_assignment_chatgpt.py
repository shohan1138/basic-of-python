# Assignment 2 - Restaurant Discount Program (Simple Version)

day = input("Enter the day of the week (first 2 letters, e.g., mo, tu, we, th, fr, sa, su): ").lower()
time = int(input("Enter the time in 24-hour format (0–23): "))

if(day=='' or time==''):
    print("Reservation must fulfill")
else:
    # Weekdays (Monday to Friday)
    if(day=='mo' or day=='tu' or day=='we' or day=='th' or day=='fr'):
        if(time < 17):
            print("NO Discount")
        elif(time >= 17):
            print("10% Discount")

    # Weekends (Saturday and Sunday)
    elif(day=='sa' or day=='su'):
        if(time < 15):
            print("5% Discount")
        elif(time >= 15):
            print("7% Discount")

    # Invalid input
    else:
        print("Invalid day entered")
