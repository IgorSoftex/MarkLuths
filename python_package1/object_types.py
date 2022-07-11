# mylist = [1, 3, 'моя строка']
# print(mylist)
# print(type(mylist))

# Форматирование
# mylen = "%s Ігор %s" % ("_", "_")
# mylen = "{0} Ігор {1}".format("_", "_")
# mylen = "{} Ігор {}".format("_", "_")
# print(mylen)

# # Пример
# mynum = 111.222
# print(mynum)

# print(dir())
# print(dir(mynum))
# print(mynum.is_integer())
# ...

# mylen = "spam"
# print(mylen + "_")
# print(mylen.__add__("__"))
# help(mylen.title)
# help(mylen.count)
# mylen = '5A\nB\tC'
# mylen = """первая строка
# вторая строка"""
# г'С: \text\new'
# mylen = r'С: \text\new'
# mylen = 'spam'
# mylen = 'sp\xc4\u00c4\U000000c4m'
# print(mylen)

# import re
# len1 = 'My Python'
# len2 = 'My Python2'
# match = re.match(len1+'*', len2)
# if match:
#     print(match.group())
# else:
#     print('None')

# print(match)
# print(match.group())
# print(type(match))

# mylist = ['123', 'spam', '1.23']
# print(mylist)
# mylist.reverse()
# print(mylist)

# mylist.sort()
# print(mylist)

# mylist.extend([555,333])
# print(mylist)

# help(mylist.reverse)

# mylist.insert(0,'новий')
# print(mylist)
# mylist.append('новий')
# print(mylist)
# mylist.pop(0)
# print(mylist)

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# diag = [matrix[i] [i] for i in [0, 1, 2]] # Собрать диагональ из матрицы
# print(diag)

# mystr = 'spam'
# res = [i for i in mystr]
# print(res)

# lst = [row[1] for row in matrix if row[1]%2 == 0] # Отфильтровать нечетные элементы
# print(lst)

# lst = [row[1]+1 for row in matrix]
# print(lst)

# column2 = [row[1] for row in matrix]
# print(column2)

# print(matrix)
# print(matrix[0][1])
# print(matrix[1][1])
# print(matrix[2][1])

# help(list)

# mylist = list(range(1, 11))
# print(mylist)

# Создать множество сумм элементов в строках:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
res = [sum(row) for row in matrix]
print(res)
