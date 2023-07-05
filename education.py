# # Stepik
#
# # Функции
#
# # 13.1
# # объявление функции
# def draw_box():
#     print('*' * 10)
#     for i in range(12):
#         print('*' + ' ' * 8 + '*')
#     print('*' * 10)
#
#
# # основная программа
# draw_box()  # вызов функции
#
# ###
#
# # объявление функции
# def draw_triangle():
#     for i in range(1, 11):
#         print('*' * i)
#
#
# # основная программа
# draw_triangle()  # вызов функции
#
# # 13.2
# # объявление функции
# def draw_triangle(fill, base):
#     for i in range(base):
#         for j in range(i + 1):
#             if j >= base - i:
#                 continue
#             print(fill, end="")
#         print()
#
#
# # считываем данные
# fill = input()
# base = int(input())
#
# # вызываем функцию
# draw_triangle(fill, base)
#
# ###
#
# # объявление функции
# def print_fio(name, surname, patronymic):
#     name = name.title()
#     surname = surname.title()
#     patronymic = patronymic.title()
#     print(surname[0] + name[0] + patronymic[0])
#
# # считываем данные
# name, surname, patronymic = input(), input(), input()
#
# # вызываем функцию
# print_fio(name, surname, patronymic)
#
# ###
#
# total = 0
#
# # объявление функции
# def print_digit_sum(num):
#     total = 0
#     while num > 0:
#         digit = num % 10
#         total += digit
#         num //= 10
#     print(total)
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print_digit_sum(n)


# 13.5
# # объявление функции
# def is_prime(num):
#     counter = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             counter += 1
#     if counter == 2:
#         return True
#     else:
#         return False
#
# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(is_prime(n))

###
# def is_prime(num):
#     counter = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             counter += 1
#     if counter == 2:
#         return True
#     else:
#         return False
#
#
# def get_next_prime(num):
#     num = num + 1
#     while is_prime(num) != True:
#         num += 1
#         if is_prime(num):
#             break
#     return num


# # считываем данные
# n = int(input())
#
# # вызываем функцию
# print(get_next_prime(n))
# is_prime(n)


###

# # объявление функции
# def is_password_good(password):
#     if len(password) < 8:
#         return False
#     else:
#         count_digit = 0
#         count_upp = 0
#         count_low = 0
#         for i in password:
#             if i.isdigit():
#                 count_digit += 1
#             if i.isupper():
#                 count_upp += 1
#             if i.islower():
#                 count_low += 1
#         if count_digit >= 1 and count_upp >= 1 and count_low >= 1:
#             return True
#         else:
#             return False
#
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(is_password_good(txt))

###

# def is_one_away(word1, word2):
#     if len(word1) != len(word2):
#         return False
#     else:
#         counter = 0
#         for i in range(len(word1)):
#             if word1[i] == word2[i]:
#                 counter += 1
#         if len(word1) - counter == 1:
#             return True
#         else:
#             return False
#
#
#
# # считываем данные
# txt1 = input()
# txt2 = input()
#
# # вызываем функцию
# print(is_one_away(txt1, txt2))

###

# def is_prime(num):
#     counter = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             counter += 1
#     if counter == 2:
#         return True
#     else:
#         return False
#
#
# # объявление функции
# def is_valid_password(password):
#     if len(password) != 3:
#         return False
#
#     else:
#         counter = 0
#
#         for i in password:
#             if not i.isdigit():
#                 return False
#
#         if password[0] == password[0][::-1]:
#             counter += 1
#
#         if is_prime == True:
#             counter += 1
#
#         if int(password[2]) % 2 == 0:
#             counter += 1
#
#         if counter == 3:
#             return True
#
#         else:
#             return False
#
#
# # считываем данные
# psw = input().split(':')
#
# # вызываем функцию
# print(is_valid_password(psw))
# is_prime(int(psw[1]))


# # объявление функции
# def convert_to_python_case(text):
#     s = text[0].lower()
#     for i in text[1:]:
#         if i.isupper() == True:
#             s = s + '_' + i.lower()
#         else:
#             s += i
#     return s
#
#
# # считываем данные
# txt = input()
#
# # вызываем функцию
# print(convert_to_python_case(txt))

###

# 13.5

# # объявление функции
# def get_middle_point(x1, y1, x2, y2):
#     x = float((x1 + x2)/2)
#     y = float((y1 + y2)/2)
#     return x, y
#
# # считываем данные
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())
#
# # вызываем функцию
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)

###

# from math import pi
#
# # объявление функции
# def get_circle(radius):
#     c = 2 * pi * radius
#     s = pi * radius ** 2
#     return c, s
#
# # считываем данные
# r = float(input())
#
# # вызываем функцию
# length, square = get_circle(r)
# print(length, square)

###

# # объявление функции
# def solve(a, b, c):
#     D = b ** 2 - (4 * a * c)
#     if D > 0:
#         y1 = (-b - (D ** 0.5)) / (2 * a)
#         y2 = (-b + (D ** 0.5)) / (2 * a)
#         minimum = min(y1, y2)
#         maximum = max(y1, y2)
#         return minimum, maximum
#     elif D == 0:
#         dskr = -b / (2 * a)
#         return dskr
#
# # считываем данные
# a, b, c = int(input()), int(input()), int(input())
#
# # вызываем функцию
# x1, x2 = solve(a, b, c)
# print(x1, x2)

# 05.07.23

# 1
# def summa(digit1, digit2):
#     total = digit1 + digit2
#     print(total)
#
#
# a = int(input())
# b = int(input())
#
# summa(a, b)

# 2
# def chetnye(n):
#     lst = []
#     for i in n:
#         if i % 2 == 0:
#             lst.append(i)
#     return lst
#
#
# num = list(map(int, input().split(' ')))
#
# print(chetnye(num))

# 3

# def stroka(str):
#     str = str[::-1]
#     return str
#
#
# s = input()
#
# print(stroka(s))

# 4

# def factorial(num):
#     total = 1
#     for i in range(1, num + 1):
#         total = total * i
#     return total
#
#
# n = int(input())
#
# print(factorial(n))

# 5
# def sort_strings(strings):
#     strings.sort()
#     return strings
#
#
# strings = input().split(' ')
#
# print(sort_strings(strings))

# 6

# def get_arithmetic_mean(numbers):
#     average = sum(numbers) / len(numbers)
#     return average
#
#
# numbers = list(map(int, input().split(' ')))
#
# print(get_arithmetic_mean(numbers))

# 7

# def vowel_counter(string):
#     counter = 0
#     for i in range(len(string)):
#         if string[i] in 'аоуиэыеюя':
#             counter += 1
#     return counter
#
#
# str = input().lower()
#
# print(vowel_counter(str))

# 8

# def positive_numbers(num):
#     numbers = []
#     for i in num:
#         if i >= 0:
#             numbers.append(i)
#     return numbers
#
#
# n = list(map(int, input().split(' ')))
#
# print(positive_numbers(n))

# 9

# def is_prime(num):
#     counter = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             counter += 1
#     if counter == 2:
#         return True
#     else:
#         return False
#
#
# n = int(input())
#
# print(is_prime(n))

# 10

# def get_unique_elements(num):
#     unique_elements = []
#     for i in num:
#         if i not in unique_elements:
#             unique_elements.append(i)
#     return unique_elements
#
#
# n = list(map(int, input().split(' ')))
#
# print(get_unique_elements(n))