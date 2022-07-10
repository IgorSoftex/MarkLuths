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

import re
len1 = 'My Python'
len2 = 'My Python'
match = re.match(len1, len2)
if match:
    print(match.group())
else:
    print('None')

# print(match)
# print(match.group())
# print(type(match))
