# Example of using the range function in a for loop

# Looping from 0 to 4 (range(n) generates numbers from 0 to n-1)
for i in range(5):
    print(f"Current number: {i}")
print("End of loop")

# Looping with a start and end value (range(start, end) generates numbers from start to end-1)
for i in range(2, 6):
    print(f"Current number: {i}")
print("End of loop")

# Looping with a step value (range(start, end, step) generates numbers with a step increment)
for i in range(1, 10, 2):
    print(f"Current number: {i}")
print("End of loop")


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit,end=' ')