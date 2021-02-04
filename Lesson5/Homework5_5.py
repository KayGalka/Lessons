'''
Урок 5. Задание №5
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

with open(r"C:\Users\kaygorodova\Desktop\Lessons_Python\Lesson5\Homework5_5.txt", "w+", encoding="utf-8") as f_obj:
    numbers = '15 25 107 33 4444 55555'
    f_obj.writelines(numbers)
    f_obj.seek(0)
    numbers = [int(numb) for numb in f_obj.readline().split()]
    print(f'Сумма всех чисел : {sum(numbers)}')