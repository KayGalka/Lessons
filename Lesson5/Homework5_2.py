'''
Урок 5. Задание №2
Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
'''

f_obj = open(r"C:\Users\kaygorodova\Desktop\Lessons_Python\Lesson5\Homework5_2.txt", encoding="utf-8")
lines = 0
for lin, content in enumerate(f_obj.readlines(), 1):
    lines = lin
    print(f'В {lin} строке {len(content.split())} слов.')
print(f'Всего строк в файле - {lines}.')