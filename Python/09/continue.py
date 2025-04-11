# Example of using the continue statement in a loop

for number in range(1, 11):  # Loop through numbers 1 to 10
    if number % 2 == 0:  # Check if the number is even
        continue  # Skip the rest of the loop for even numbers
    print(number)  # Print only odd numbers