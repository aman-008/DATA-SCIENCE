def sum(a,b):
    # a and b are local variables
    c = a + b
    z = 1 # it creates a local variable called z which is destroyed after this function returns 
    return c
z = 8 # z is global variable
print(sum(2,3))
print(z)