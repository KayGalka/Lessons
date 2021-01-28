# Урок 3. Задание №3
# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.sort(reverse=True)
    summa = my_list[0] + my_list[1]
    return summa


argument_1 = int(input('Введите первое число: '))
argument_2 = int(input('Введите второе число: '))
argument_3 = int(input('Введите третье число: '))

print('Сумма наибольших двух аргументов равна:  ', my_func(argument_1, argument_2, argument_3))