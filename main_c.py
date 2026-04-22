print("Добро пожаловать в канкулятор Ивана Петровича!")

def fun_minus():
    a = int(input("Введите 1 число, из которого будет вычитаться "))
    b = int(input("Введите второе число, что будет вычитать "))
    print(f"{a} - {b} = {a-b}")

def fun_divide():
    a = int(input("Введите натуральное число на которое будутт делить "))
    if a == 0:
        print("НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ!")
        fun_divide()
    b = int(input("Введите число что будет делить "))
    print(f"{a} / {b} = {a/b}")

while True:
print("Добро пожаловать в канкулятор Ивана Петровича!")

def fun_multiply():
    a = int(input("Введите первое число для умножения "))
    b = int(input("Введите второе число для умножения "))
    print(f"{a} * {b} = {a*b}")

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
        fun_multiply()
    elif action == 3:
        fun_divide()
    else:
        print("Вы ввели не валидные данные")
        print("Дух машины растроен и покидает вас")