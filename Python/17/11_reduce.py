from functools import reduce
number = [1, 23, 4, 66, 34, 2, 6, 9, 54]
      #  [24 + 4, 66, 34, 2, 6, 9, 54]
      #  [28 + 66, 34, 2, 6, 9, 54]
      #  [94 + 34, 2, 6, 9, 54]
      #  [128 + 2, 6, 9, 54]
      #  [130 + 6, 9, 54]
      #  [136 + 9, 54]
      #  [145 + 54]
      #  [199]
def sum(x, y):
    return x + y

c = reduce(sum, number)
print(c)
