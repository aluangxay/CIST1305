# random.py
import random

def main():
    # Create a list with 5 random numbers.
    numbers = [random.randint(1, 100) for _ in range(5)]

    # Display the first element of the number list.
    print('The first number generated is: ', numbers[0])

    # Display the generated numbers.
    print('The generated numbers are:', numbers)

    # Get the sum of the elements.
    sum = getTotal(numbers)

    # Display the sum of the list elements.
    print('The total is', sum)

    # Append a new random number to the list.
    newNumber = random.randint(1, 100)
    numbers.append(newNumber)

    # Display the new number that was appended.
    print('Appending a new number: ', newNumber)

    # Display updated number list
    print('The updated numbers are:', numbers)

    # Get the sum of the elements.
    sum = getTotal(numbers)

    # Display the sum of the list elements.
    print('The total is', sum)

# The get_total function accepts a list as an
# argument and returns the total of the values in
# the list.
def getTotal(valueList):
    # Create a variable to use as an accumulator.
    total = 0
    
    # Calculate the total of the list elements.
    for num in valueList:
        total += num

    # Return the total.
    return total

# Call the main function.
main()
