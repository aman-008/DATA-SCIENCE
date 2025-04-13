# while True:
#     try:
#         first_number = int(input("Enter number 1: "))
#         second_number = int(input("Enter number 2: "))
#         print(f"The sum is {first_number / second_number}")
        
#     except ValueError:
#         print("Please don't Perform bad typecasts")
        
#     except ZeroDivisionError:
#         print("Hey don't divide by 0")
#     except Exception as e:
#         print("Unknown error occurred!",e)
    


first_number = int(input("Enter number 1: "))
second_number = int(input("Enter number 2: "))

if second_number == 0:
    raise ValueError("Please don't divide by 0")
print(f"The sum is {first_number / second_number}")