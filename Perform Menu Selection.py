# Convert inches to centimeters
# Convert feet to meters
# Convert miles to kilometers

# centimeters = inches × 2.54
# meters = feet × 0.3048
# kilometers = miles × 1.609

# The program should display a menu, such as the following, that allows the user to select
# the conversion that he or she wants to perform.
#   1. Convert inches to centimeters.
#   2. Convert feet to meters.
#   3. Convert miles to kilometers.
#   Enter your selection.

# // Declare a variable to hold the
# // user's menu selection.
# Declare Integer menuSelection

# // Declare variables to hold the units
# // of measurement.
# Declare Real inches, centimeters, feet, meters, miles, kilometers

# // Display the menu.
# Display "1. Convert inches to centimeters."
# Display "2. Convert feet to meters."
# Display "3. Convert miles to kilometers."
# Display

# // Prompt the user for a selection 
    # Display "Enter your selection."
    # Input menuSelection
# // Perform the selected operation.
# Display "Enter the number of inches."
# Select menuSelection
# Case 1:
    # // Convert inches to centimeters.
    # Input inches
    # Set centimeters = inches * 2.54
    # Display "That is equal to ", centimeters, " centimeters."
    # Perform the selected operation.
# Case 2:
    # // Convert feet to meters.
    # Display "Enter the number of feet."
    # Input feet
    # Set meters = feet * 0.3048
    # Display "That is equal to ", meters, " meters."
# Case 3:
    # // Convert miles to kilometers.
    # Display "Enter the number of miles."
    # Input miles
    # Set kilometers = miles * 1.609
    # Display "That is equal to ", kilometers, " kilometers."

# Default:
# // Display an error message.
# Display "That is an invalid selection."
# End Select

def menu():           
    print("1. Convert inches to centimeters.")
    print("2. Convert feet to meters.")
    print("3. Convert miles to kilometers.")
    print()

    menuSelection = input("Enter your selection:")

    if menuSelection == "1" :
        inches = float(input("Enter the number of inches: "))
        centimeters = inches * 2.54
        print(f"That is equal to {centimeters} centimeters.")

    elif menuSelection == "2" :
        feet = float(input("Enter the number of feet: "))
        meters = feet * 0.3048
        print(f"That is equal to {meters} meters.")

    elif menuSelection == "3" :
        miles = float(input("Enter the number of miles: "))
        kilometers = miles * 1.60934
        print(f"That is equal to {kilometers} kilometers.")

    else:
        print("That is an invalid selection.")

menu()