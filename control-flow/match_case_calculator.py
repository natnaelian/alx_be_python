numb1 = float(input("Enter the first number: "))
numb2 = float(input("Enter the second number: "))
x = input("Choose the operation (+, -, *, /):")
match x:
    case "+":
        print(f"The result is {numb1 + numb2}")
    case "-":
        print(f"The result is {numb1 - numb2}")
    case "*":
        print(f"The result is {numb1 * numb2}")
    case "/":
        if numb2 != 0:
            print(f"The result is {numb1 / numb2}")
        else:
            print("Cannot divide by zero.")