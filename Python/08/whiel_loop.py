# Example 1: Simple counter
count = 0
while count < 5:
    print("Count is:", count)
    count += 1

# Example 2: Summing numbers
n = 1
total = 0
while n <= 10:
    total += n
    n += 1
print("Sum of numbers from 1 to 10 is:", total)

# Example 3: User input example
password = "python123"
user_input = ""
while user_input != password:
    user_input = input("Enter the password: ")
print("Access granted!")