def return_res_format(num1: float, operator: str, num2: float, res: float) -> str:
    return f"{num1} {operator} {num2} = {res}"


def want_to_exit(order) -> bool:
    if order.strip() == "q":
        return True
    return False


def main() -> None:
    print("if you want to exit the program enter q")
    while True:
        while True:
            try:
                order = input(
                    'enter the first number:("if you want to exit the program enter q") '
                ).strip()
                if want_to_exit(order):
                    return
                num1 = float(order)
                break
            except ValueError:
                print("please enter a real number")
        while True:
            op = input(
                'please enter a operator:(like:{+,-,*,/,^,%})("if you want to exit the program enter q") '
            ).strip()
            if want_to_exit(op):
                return
            if op not in ["+", "-", "*", "/", "^", "%"]:
                print("please enter a valid operator")
            else:
                break
        while True:
            order = input(
                'enter the second number:("if you want to exit the program enter q") '
            ).strip()
            if want_to_exit(order):
                return
            try:
                num2 = float(order)
                break
            except ValueError:
                print("please enter a real number")
        if op == "-":
            print(return_res_format(num1, op, num2, num1 - num2))
        elif op == "+":
            print(return_res_format(num1, op, num2, num1 + num2))
        elif op == "*":
            print(return_res_format(num1, op, num2, num1 * num2))
        elif op == "/":
            if num2 == 0:
                print("second number can't be zero")
            else:
                print(return_res_format(num1, op, num2, num1 / num2))
        elif op == "^":
            print(return_res_format(num1, op, num2, num1**num2))
        elif op == "%":
            print(return_res_format(num1, op, num2, num1 % num2))


if __name__ == "__main__":
    main()
