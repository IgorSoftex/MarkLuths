# Файлы
# filename = "C:\\Igor\\Python\\MyCode\\Марк Лутц Изучаем Python\\temp\\file1.txt"
# myfile = open(filename, 'w') # Создать новый файл в режиме записи ('w')
# myfile.write('Первая строка\n')
# myfile.write('Вторая строка\n')
# myfile.close() # Закрыть для сбрасывания буферов вывода на диск

# Прочитаем файл (сразу весь)
# filename = "C:\\Igor\\Python\\MyCode\\Марк Лутц Изучаем Python\\temp\\file1.txt"
# with open(filename, 'r') as file_object:
#     contents = file_object.read() # сразу весь файл
#     print(contents)

# Прочитаем файл (построчно)
# filename = "C:\\Igor\\Python\\MyCode\\Марк Лутц Изучаем Python\\temp\\file1.txt"
# with open(filename, 'r') as file_object:
#     for line in file_object:
#         print(line)

# Прочитаем файл (построчно) с помощью конструкции for
# filename = "C:\\Igor\\Python\\MyCode\\Марк Лутц Изучаем Python\\temp\\file1.txt"
# for line in open(filename, 'r'):
#     print(line)

# with open(filename, 'r') as file_object:
#     for line in file_object:
#         print(line)

# Текст Unicode
# symbol = 'sp\xc4m'
# print(symbol)
# filename = "C:\\Igor\\Python\\MyCode\\Марк Лутц Изучаем Python\\temp\\file1.txt"
# with open(filename, 'w', encoding='utf-8') as file_object:
#     file_object.write(symbol)

# filename = "C:\\Igor\\Python\\MyCode\\Марк Лутц Изучаем Python\\temp\\file1.txt"
# with open(filename, 'r', encoding='utf-8') as file_object:
#     contents = file_object.read()
#     print(contents)

filename = "C:\\Igor\\Python\\MyCode\\Марк Лутц Изучаем Python\\temp\\file1.txt"
with open(filename, 'rb') as file_object:
    contents = file_object.read()
    print(contents)
    print(contents.decode('utf-8'))
