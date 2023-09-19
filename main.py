# 13/09/23

# 1

# def factorial(n):
#     fact = 1
#     for i in range(1, n + 1):
#         fact *= i
#     print(f'Факториал числа {n} - {fact}')
#
#
# n = int(input())
# factorial(n)


# 2

# def func(lst):
#     for i in lst:

# 3

# def func(str):
#     words = str.split(' ')
#     counter = 0
#     unique_words = []
#     for word in words:
#         if word not in unique_words:
#             unique_words.append(word)
#             counter += 1
#     return counter
#
#
# string = 'world peace green world peace blue world peace green red'
# print(func(string))


# 4

# def func(lst):
#     a = []
#     for i in lst:
#         if i % 2 == 0:
#             a.append(i)
#     return a
#
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(func(lst))


# 5


# def func(n):
#     n_str = str(n)
#
#     if n_str == n_str[::-1]:
#         return True
#     else:
#         return False
#
#
# num = int(input())
# print(func(num))


# 7

# def func(lst1, lst2):
#     a = []
#     for i in lst1:
#         if i in lst2 and i not in a:
#             a.append(i)
#     return a
#
#
# list1 = [1, 2, 3, 4, 24, 34, 54]
# list2 = [11, 25, 34, 1, 24, 56, 44]
# print(func(list1, list2))

# 8
# def func(n):
#     a, b = 0, 1
#     while b < n:
#         a, b = b, a + b
#     if b == n:
#         return True
#     else:
#         return False
#
#
# number = int(input())
# print(func(number))


# 9

# def func(lst):
#     a = []
#     for i in lst:
#         count = 0
#         for j in i:
#
#             if 'a' in i.lower():
#                 count += 1
#                 if count > 1:
#                     break
#         if count > 1:
#             a.append(i)
#     return a
#
# list = ['fjfjidijf', 'doAijdfafa', 'afiifjod', 'fsdkkAfkjdk']
# print(func(list))

# 12

# def func(lst1, lst2):
#     a = []
#     for i in lst1:
#         if i in lst2 and i not in a:
#             a.append(i)
#     return a
#
#
# list1 = [1, 2, 3, 4, 5, 7, 89]
# list2 = [11, 2, 364, 1, 24, 56, 44]
# print(func(list1, list2))

# 13

# def func(lst):
#     a = []
#     for s in lst:
#         a.append(s[::-1])
#     return a
#
# list = ['afc', 'frok']
# print(func(list))

# 14
# def func(n):
#     total = 0
#     while n != 0:
#         digit = n % 10
#         total += digit
#         n //= 10
#     return total
#
# n = int(input())
# print(func(n))

# 15

# def func(lst):
#     a = []
#     for i in lst:
#         n = i
#         while i > 1:
#             if i % 2 != 0:
#                 break
#             i /= 2
#         if i == 1:
#             a.append(n)
#     return a
#
# list = [2, 32, 45, 78, 40]
# print(func(list))


# 16

# from datetime import datetime
#
#
# def func(input_date):
#     input_datetime = datetime.strptime(input_date, "%Y-%m-%d")
#
#     now = datetime.now()
#
#     delta = now - input_datetime
#
#     return delta.days
#
#
# date = input('Введите дату в формате ГГГГ-ММ-ДД: ')
# print(func(date))

# 19/09/23

# 1

# def func(student_dict):
#     total = 0
#     counter = 0
#     for student in student_dict:
#         grade = student_dict[student]
#         total += grade
#         counter += 1
#     return total / counter
#
#
# student_dict = {
#     "Антон": 70,
#     "Борис": 76,
#     "Слава": 56,
#     "Веня": 83,
#     "Иван": 97
# }
#
# print(func(student_dict))

# 2

# def func(price_dict):
#     max_price = 0
#     for product in price_dict:
#         price = price_dict[product]
#
#         if price > max_price:
#             max_price = price
#             most_expensive_product = product
#
#     return most_expensive_product
#
#
# price_dict = {
#     "Сметана": 70,
#     "Батон": 76,
#     "Хлеб": 56,
#     "Молоко": 83,
#     "Сыр": 97
# }
#
# print(func(price_dict))

# 3

# def func(goods_sold_dict):
#     total_all = 0
#     for product in goods_sold_dict:
#         products_total = goods_sold_dict[product]
#         total_all += products_total
#     return total_all
#
#
# goods_sold_dict = {
#     "Самокаты": 70,
#     "Велосипеды": 76,
#     "Гироскутеры": 56,
#     "Скейты": 83,
#     "Инвалидные коляски для СВО-шников": 97
# }
#
# print(func(goods_sold_dict))

# 4

# def func(population_dict):
#     max_num = 0
#     for population in population_dict:
#
#         num = population_dict[population]
#
#         if num > max_num:
#             max_num = num
#             most_populatios_city = population
#
#     return most_populatios_city
#
# population_dict = {
#     "Мухосранск": 70,
#     "Подзалупинск": 76,
#     "Чита": 56,
#     "Хабаровск": 83,
#     "Мариуполь": 97
# }
#
# print(func(population_dict))

# 5

# def func(tasks_dict):
#     max_time = 0
#     for task in tasks_dict:
#
#         num = tasks_dict[task]
#
#         if num > max_time:
#             max_time = num
#             most_long_task = task
#
#     return most_long_task
#
#
# tasks_dict = {
#     "Почистить зубы": 70,
#     "Завтрак": 76,
#     "Собрать рюкзак": 56,
#     "Сделать физику": 83,
#     "Сдать зачет": 97
# }
#
# print(func(tasks_dict))