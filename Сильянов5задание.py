'''
Группа 21ИС-21
Сильянов Ярослав
15.11.2022
Задача №5:
Даны три целых числа, одно из которых отлично от двух других, равных между собой. Определить порядковый номер числа, отличного от остальных.
'''
a = int(input())
b = int(input())
c = int(input())
if a == b:
    print(3)
elif a == c:
    print(2)
else:
    print(1)
