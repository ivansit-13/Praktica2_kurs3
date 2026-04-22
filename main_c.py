print("Добро пожаловать в канкулятор Ивана Петровича!")

def fun_minus():
    a = int(input("Введите 1 число, из которого будет вычитаться "))
    b = int(input("Введите второе число, что будет вычитать "))
    print(f"{a} - {b} = {a-b}")

while True:
    print("Пожалуйста выберите действие написав цифру 0-3")
    print("0 - вычитание")
    print("1 - сложение")
    print("2 - умножение")
    print("3 - деление")


    action = int(input("Вы выбираете = "))
    if action == 0:
        fun_minus()
    elif action == 1:
        pass
    elif action == 2:
        pass
    elif action == 3:
        pass
    else:
        print("Вы ввели не валидные данные")
        print("Дух машины растроен и покидает вас")