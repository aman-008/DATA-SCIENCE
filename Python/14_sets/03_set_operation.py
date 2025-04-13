# Define two sets with some numbers
a = {3, 23, 1}
b = {1, 2, 3, 4}

# union() combines all unique elements from both sets (no duplicates)
c = a.union(b)
print(c)  # Output: {1, 2, 3, 4, 23} → all elements from both a and b

# intersection() gives only the elements that are common in both sets
d = a.intersection(b)
print(d)  # Output: {1, 3} → these are found in both a and b

# difference() gives elements that are in 'a' but NOT in 'b'
e = a.difference(b)
print(e)  # Output: {23} → 23 is in a, but NOT in b
f = b.difference(a)
print(f)
