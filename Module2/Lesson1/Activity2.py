print("Choose your ride:")
print("1.Bike")
print("2.Car")

choice = int(input("Enter your choice:"))
if (choice == 1):
    print("What type of bike?")
    print("Scooty")
    print("Scooter")

    choice2 = int(input("Enter your choice:"))
    if (choice2 == 1):
        print("You have selected a scooty")
    else:
        print("You have selected a scooter")

elif (choice == 2):
    print("What type of car?")
    print("BMW")
    print("Toyota")

    choice3 = int(input("Enter your choice:"))
    if (choice3 == 1):
        print("You have selected BMW")
    else:
        print("You have selected Toyota")
else:
    print("Wrong choice")
