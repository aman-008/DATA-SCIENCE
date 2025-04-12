s = {34, 23, 1, 3, 22}
s.add(45)
s.add(322)
print(s)
s.remove(1)
print('after removing 1 from set:', s)
# s.remove(3434)
# print('after removing 3434 from set:', s) # this will raise KeyError because 3434 is not in the set
s.discard(32)
print('after discarding 32 from set:', s) # this will not raise KeyError because discard does not raise an error if the element is not found
s.pop() # this will remove a random element from the set
print('after popping an element from set:', s)
