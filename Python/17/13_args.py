def sum(*args):
    """Sum all the arguments."""
    # args will be a tuple of all the values passed to sum
    total = 0
    for arg in args:
        total += arg
    return total
a = sum(1,2,8,56)
print(a)