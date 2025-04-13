numbers = [1, 2, 3, 34, 45, 21]

# def square(x):
#     return x * x

# new = list(map(square,numbers))


# new = list(map(lambda x: x*x, numbers))
# print(new)



input_str = input("Enter numbers separated by space: ")
nums = list(map(int, input_str.split()))
print(nums)