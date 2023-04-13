from fractional_num import FractionalNum


if __name__ == "__main__":
    n1 = int(input("Введите первое число: "))
    n2 = int(input("Введите первое число: "))
    num1 = FractionalNum(n1, n2)
    print(f"Первое число: {num1}")
    n1 = int(input("Введите второе число: "))
    n2 = int(input("Введите второе число: "))
    num2 = FractionalNum(n1, n2)
    print(f"Второе число: {num2}")

    flag = "y"
    while flag != "n":
        print("1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n5. Ввести новые числа\nn. Закончить")
        flag = input("Введите ваш выбор: ")

        if flag == "1":
            print(f"\n{num1 + num2}\n")
        if flag == "2":
            print(f"\n{num1 - num2}\n")
        if flag == "3":
            print(f"\n{num1 * num2}\n")
        if flag == "4":
            print(f"\n{num1 / num2}\n")
        if flag == "5":
            n1 = int(input("Введите первое число: "))
            n2 = int(input("Введите первое число: "))
            num1 = FractionalNum(n1, n2)
            print(f"Первое число: {num1}")
            n1 = int(input("Введите второе число: "))
            n2 = int(input("Введите второе число: "))
            num2 = FractionalNum(n1, n2)
            print(f"Второе число: {num2}")
