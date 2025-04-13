try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    print("What kind of operation do you want to perform?\nPress + for addition\nPress - for subtraction\nPress * for multiplication\nPress / for division")
    operator = input("Enter the operator: ")
    match operator:
        case '+':
            print(f"The result is: {a + b}")
        case '-':
            print(f"The result is: {a - b}")
        case '*':
            print(f"The result is: {a * b}")
        case '/':
            print(f"The result is: {a / b}")
        case default:
            print("This is not a valid operator")
except Exception as e:
    print("This is not a valid operator")
