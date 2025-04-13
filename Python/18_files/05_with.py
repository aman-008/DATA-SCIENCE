# f = open("aman.txt", "r")
# content = f.read()
# print(content)
# f.close()


with open("aman.txt", "r") as f:
    content = f.read()
    print(content)
    # No need to write f.close() because file is already closed by default when using with syntax