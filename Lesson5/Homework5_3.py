'''
Урок 5. Задание №3
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''

with open(r"C:\Users\kaygorodova\Desktop\Lessons_Python\Lesson5\Homework5_3.txt", encoding="utf-8") as f_obj:
    my_list = []
    for surname in f_obj.readlines():
        my_list.append(float(surname.split()[1]))
        if float(surname.split()[1]) < 20000:
            print(f'Сотрудники с окладом менее 20 тыс: - {surname.split()[0]}.')
    print(f'Средняя величина дохода сотрудников - {int(sum(my_list) // len(my_list))} рублей.')