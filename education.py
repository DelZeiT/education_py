# Stepik

# Функции

# 13.1
# объявление функции
def draw_box():
    print('*' * 10)
    for i in range(12):
        print('*' + ' ' * 8 + '*')
    print('*' * 10)


# основная программа
draw_box()  # вызов функции

###

# объявление функции
def draw_triangle():
    for i in range(1, 11):
        print('*' * i)


# основная программа
draw_triangle()  # вызов функции

# 13.2
# объявление функции
def draw_triangle(fill, base):
    for i in range(base):
        for j in range(i + 1):
            if j >= base - i:
                continue
            print(fill, end="")
        print()


# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)

###

# объявление функции
def print_fio(name, surname, patronymic):
    name = name.title()
    surname = surname.title()
    patronymic = patronymic.title()
    print(surname[0] + name[0] + patronymic[0])

# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)

###

total = 0

# объявление функции
def print_digit_sum(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num //= 10
    print(total)
# считываем данные
n = int(input())

# вызываем функцию
print_digit_sum(n)

