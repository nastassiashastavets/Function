# def a_function():
#     print('You just created a function')
# a_function() #вызов функции

# def empty_function():
#     pass

#создать функцию, которая будет сразу считать сумму чисел в массиве
# def b_function():
#     print('Сумма чисел равняется ', sum([1, 4, 7, 3, 8, 9]))
# b_function()

# def add(a, b):
#     return "пример с операциями", a + b, a * b , a / b
# print(add(5, 6))

# def add(a, b):
#     return a + b
# print(add(a=5, b = 9))
# total = add(b=4, a = 6)
# print(total)

#аргументы - это значения
#параметры - переменные
# def keyword_function( a = 2, b = 3):
#     return a+ b
#
# print(keyword_function(a = 5, b = 6))
# print(keyword_function())

# def mixed_function( a, b=2, c =3):
#     return a + b + c
# print(mixed_function(1, b=7, c=8))
# print(mixed_function(1))

#*args-арги-числа
#**kwargs-кварги-словарь


# def function_a():
#     global a
#     a = 1
#     b = 2
#     return a + b
# def function_b():
#     c = 3
#     return a + c
# print(function_a())
# print(function_b())

# def is_year_leap(year):
#     return year % 100 != 0 and year % 4 == 0 and year % 400 == 0
# print(is_year_leap(1995))

# import math
# def square(b):
#     return b * 4, b **2,  math.sqrt(2)*b
# b = int(input('Введите сторону квадрата: '))
# print(square(b))
# def simple_decore(fn):
#     def wrapper():
#         print("start function")
#         fn()
#         print("stop function")
#     return wrapper
#
# @simple_decore
# def first_test():
#     print('test function 1')
#
# @simple_decore
# def second_test():
#     print('test function 2')
# first_test()
# second_test()

# #1.Написать функцию, которая определяет количество разрядов введенного целого числа.
# def digits(n):
#     i = 0
#     while n > 0 :
#         n = n // 10
#         i += 1
#     return i
# num = abs(int(input('введите число')))
# print('Количество разрядов:', digits(num))

#2 В зависимости от выбора пользователя вычислить площадь круга, прямоугольника или треугольника.
# Для вычисления площади каждой фигуры должна быть написана отдельная функция.


#4 Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
# и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень). Номер месяца вводить с клавиатуры.
#
# def season(n):
#     if n == 12 or 1 <= n <=2:
#         print( 'Зима')
#     elif 3 <= n <= 5:
#         print('Весна')
#     elif 6 <=n <= 8:
#         print('Лето')
#     elif 9<=n<=11:
#         print('Осень')
#     else:
#         print('Такого месяца не существует')
#
# n = int(input('Введите номер месяца'))
# season(n)

#6. Функция, вычисляющая среднее арифметическое элементов списка.
# Список должен состоять из случайных чисел, длинной 10 элементов.
# import random
# N = [random.randint(1, 100) for i in range(10)]
# def average():
#     s = 0
#     for i in N:
#         s += i
#     return s / 10
#
# print(N)
# print(average())

#д\з.1.Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).

# k = float(input('Введите число вещественного типа'))
# e = float(input('Введите еще одно число вещественного типа'))
# y = input('Введите операцию')
# def calculation(k, e):
#     while True:
#         if y == '+':
#             return k+ e
#         elif y == '-':
#             return k-e
#         elif y == '*':
#             return k*e
#         elif y == '/' and e !=0:
#             return k/e
#         elif e == 0 and y == '/':
#             return 'На ноль делить нельзя'
# print(calculation(k, e))
#
#д\з.2.
#Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – количество букв.
# Сделать проверку со всеми этими случаями.
N = str(input('Введите данные'))
def function(N):
    if type(N) == tuple():
        return(len(N.split))
    elif type(N) == list:
        return('Количество букв:', len(letters.find(N)) and N.isdigit())
        return('Количество цифр:',len(numbers.find(N)) and N.isalpha())
    elif type(N) == int() :
        for i in N:
            if int(N) % 2 == 0:
                i += 1
        return ('Количество нечетных цифр:', len(i))

    elif type(N) == str():
        return ('Количество букв:', len(N))

function(N)
print(function(N))




