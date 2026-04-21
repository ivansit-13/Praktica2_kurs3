print("Добро пожаловать в канкулятор Ивана Петровича!")

def plus_func():
    a = int(input("Введите первое число "))
    b = int(input("Введите второе число "))
    print(f"{a} + {b} = {a+b}")

while True:
    print("Пожалуйста выберите действие написав цифру 0-3")
    print("0 - вычитание")
    print("1 - сложение")
    print("2 - умножение")
    print("3 - деление")


    action = int(input("Вы выбираете = "))
    if action == 0:
        pass
    elif action == 1:
        plus_func()
    elif action == 2:
        pass
    elif action == 3:
        pass
    else:
        print("Вы ввели не валидные данные")
        print("Дух машины растроен и покидает вас")