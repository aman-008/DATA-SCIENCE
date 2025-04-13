# def is_greater_than_9(x):
#     if x > 9:
#         return True
#     else:
#         return False

number = [1, 23, 4, 66, 34, 2, 6, 9, 54]
# new = list(filter(is_greater_than_9, number))
new = list(filter(lambda x : x > 9, number))
print(new)