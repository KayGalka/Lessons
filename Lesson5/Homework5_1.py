'''
Урок 5. Задание №1
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''

try:
    with open(r"C:\Users\kaygorodova\Desktop\Lessons_Python\Lesson5\Homework5_1.txt", "w", encoding="utf-8") as file:
        while True:
            string = input("Введите текст. Для оконания введите пустую строку: ")
            if string == "":
                break
            else:
                file.write(string + "\n")
except (EOFError, FileNotFoundError):
    print("Произошла ошибка ввода-вывода!")