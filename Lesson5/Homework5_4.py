'''
Урок 5. Задание №4
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''

my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
f = open(r"C:\Users\kaygorodova\Desktop\Lessons_Python\Lesson5\Homework5_4_new.txt", "w+""", encoding="utf-8")
with open(r"C:\Users\kaygorodova\Desktop\Lessons_Python\Lesson5\Homework5_4.txt", "r+", encoding="utf-8") as f_obj:
    for content in f_obj.readlines():
        my_list = content.split()
        print(my_dict.get(my_list[0]), my_list[1], my_list[2], file=f)
f.close()