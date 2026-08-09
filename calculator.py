def return_res_format(num1: float, operator: str, num2: float, res: float) -> str:
    return f"{num1} {operator} {num2} = {res}"


while True:
    while True:
        try:
            num1 = float(input("enter the first number: ").strip())
            break
        except ValueError:
            print("please enter a real number")
    while True:
        op = input("please enter a operator:(like:{+,-,*,/}) ").strip()
        if op not in ["+", "-", "*", "/"]:
            print("please enter a valid operator")
        else:
            break
    while True:
        try:
            num2 = float(input("enter the second number: ").strip())
            break
        except ValueError:
            print("please enter a real number")
    if op == "-":
        print(return_res_format(num1, op, num2, num1 - num2))
    elif op == "+":
        print(return_res_format(num1, op, num2, num1 + num2))
    elif op == "*":
        print(return_res_format(num1, op, num2, num1 * num2))
    else:
        if num2 == 0:
            print("second number can't be zero")
            continue
        else:
            print(return_res_format(num1, op, num2, num1 / num2))
        break
