# print(5, 8, 6)
# a=123
# b=1.23
# f=None
# print(a, b, f)
# a='kj;kjhljh;kjbk;h'
# c="kjbkjbjb'lj/b"
# print(a, c)
# d=7
# print(type(d)) # определение типа переменной
# q='lhbkh;jffhd;jvb'
# print(type(q))  # определение типа переменной
# q = 'lhbkh;  \' \n jffhd;jvb'# \' для вывода кавычки, \n перенос на другую строку
# print(q)
# q='lhbkh"ff"hdjvb'
# print(q)
# """
# print(q) закомитить часть кода кавычки сверху и снизу
# print(q)
# print(q)
# """
# # print(q) выделяем часть - закомитить часть кода выделяем и нажимаем ctrl+k и ctrl+c
# # print(q) снять с одной строки или группы ctrl+k и ctrl+u

# v=5
# n=5.69
# m='hello'
# print(f"{v} - {n} - {m}")  # вывод строки в терминале 5 - 5.69 - hello
# print("{} - {} - {}".format(v, n, m)) # вывод строки в терминале 5 - 5.69 - hello
# print('Введите перве число: ')
# a=input()
# b=input("Введите второе число: ")
# print(a, '+', b, '=', a+b)  # вывод 10 + 20 = 1020
# c=5.69
# print(c) # распечатается 5,69
# n=int(c)
# print(n) # распечатается 5, так как int(c) приведение к целочисленному значению
# d=5.89
# print(d)
# print(type(d))
# d=int(d)
# print(d)
# print(type(d))
# d=5.89
# d = str(d)
# print(d)
# print(type(d))
# d = str(d)
# print(d+'69')
# print(type(d))
# e=1
# print(e)            #1
# print(type(e))  # <class 'int'>
# e=bool(e)
# print(e)           #True
# print(type(e))     #<class 'bool'>

# print('Введите первое число: ')
# a=int(input())
# b=int(input('Введите второе число: '))
# print(a, '+', b, '=', a+b)
# + Сложение 5+6=11
# - вычетание 6-5=1
# * умножение
# / деление(по умолчанию в вещественных числах) 1/4=0,25
# % Остаток от деления 5%2=1
# // Целочисленное деление 5//2=2.5
# ** Возведение в степень  2**3=8
# a=5.89956
# b=6.556551
# print(round(a*b, 5)) # roundокругляет число a*b, 5 количество знаков после запятой
# iter=2
# iter+=3 # iter=iter+3
# iter -= 4  # iter=iter-4
# iter *= 5  # iter=iter*5
# iter /= 5  # iter=iter/5
# iter //= 5  # iter=iter//5
# iter %= 5  # iter=iter%5
# iter **= 5  # iter=iter**5
# a = 1 > 4  # False
# print(a)
# b = 1 < 4 and 5 > 2 # True  and и
# print(b)
# c = 1 == 2  # False
# print(c)
# d = 1 != 2  # True
# print(d)
# e = 'qwe'
# f = 'qwe'
# print(e == f)   # True
# q = 1 < 3 < 5 < 10  # True
# print (q)
# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же Маша!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)
# i=0
# while i < 5:
#     if i == 3:   результат будет 3 так как break прервет выполнение когда i будет равна 3
#         break
#     i = i + 1
# else:
#     print('Пожалуй')   else не будет работать так как while завершился командой break не выполнив основное условие
#     print('хватит')
# print(i)
# i=0
# while i < 5:
#      i = i + 1
# else:
#     print('Пожалуй')  # Выведется
#     print('хватит')   # Выведется
# print(i)              # результат будет 5 по достижении i = 5 в цикле while
# break лучше не использовать

# Использоание флагов
# n = int(input('Введите число: '))
# flag = True
# i=2
# while flag: # Аналогично записи while flag == True
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1

# цикл for
# r = range(5) # 0 1 2 3 4
# r = range(2, 5) # 2 3 4
# r = range(0, -5) # ---- ничего так как к 0 прибавляется 1 - отрицательного значения не получится
# r = range(1, 10, 2) # 1 3 5 7 9 от 1 до 10 не включительно с шагом 2
# r = range(100, 0, -20) # 100 80 60 40 20 от 100 до 0 с шагом 20, - отрицательная сторона (в обратную сторону)
#  for i in r:    # вместо r можно написать range(100, 0, -20)
#      print(i)  # результат 100 80 60 40 20
# for i in 'qwerty':
#     print(i)
#     вывод будет
#     q
#     w
#     e
#     r
#     t
#     y
# a = 'qwerty'
# print(a[0])  # выведется q
# for i in a:
#     print(i) # распечатает строку соответственно значению i
# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "* "
#     print(line)

# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text))  # показывает размер 39
# print('ещё' in text)  # True "ещё" есть в тексте
# print(text.lower())   # съешь ещё этих мягких французских булок - все маленькими буквами
# print(text.upper())   # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК - все большими буквами
# print(text.replace('ещё', 'ЕЩЁ'))  # СъЕШЬ ЕЩЁ этих МяГкИх французских булок - печать фразы, но слово ещё печатаем большими
# text = 'съешь ещё этих мягких французских булок'
# если [2:] от 2-х до конца
# если [:10] от 0 до 10
# если [2:10] от 2 до 10
# print(text[0]) # Печать 0-го элемента фразы "с"
# print(text[1])  # Печать 1-го элемента фразы "ъ"
# print(text[len(text)-1])  # Печать последнего элемента фразы "к"
# print(text[-1])           # Печать последнего элемента фразы "к"
# print(text[-5])  # Печать 5-го с конца элемента фразы "б"
# print(text[:])  # Печать всей фразы "съешь ещё этих мягких французских булок"
# print(text[:2])  # Печать 1-х 2-х элемента фразы "съ"
# print(text[len(text)-2:])  # Печать последних 2-х элемента фразы "ок"
# print(text[2:9])  # Печать со 2-го элемента до 9-го фразы "ешь ещё"
# print(text[6:-18])  # Печать от 6-го элемента до -18-го фразы "ещё этих мягких"
# print(text[0:len(text):6])  # Печать от 0-го элемента до конца строки с шагом 6 "с"
# print(text[::6])  # Печать 0-го элемента до конца строки с шагом 6 "с"
# text = text[2:9] + text[-5] + text[:2] # печать от 2-го до 9-го элумента, далее -5-й элемент, первые 2 буквы "ешь ещёбсъ"
# print(text)
