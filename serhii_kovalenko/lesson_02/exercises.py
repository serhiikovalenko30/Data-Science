"""
**Упражнения (Условный оператор):**
"""
# Задача: проверить, может ли такой треугольник существовать
x, y, z = 3, 4, 5
if x > y + z or y > x + z or z > y + x:
    print('треугольник существует')
else:
    print('треугольник не существует')

# Задача: найти максимальное число
task_input = (1, 2, 7)
if task_input[0] > task_input[1] and task_input[0] > task_input[2]:
    print(f'{task_input[0]} максимальное число')
elif task_input[1] > task_input[2] and task_input[1] > task_input[0]:
    print(f'{task_input[1]} максимальное число')
elif task_input[2] > task_input[0] and task_input[2] > task_input[1]:
    print(f'{task_input[2]} максимальное число')
else:
    print('что-то пошло не так')

# Задача: проверить, является ли год высокосным
input_date = '2019-05-23'
print('год высокосный' if int(input_date.split('-')[0]) % 4 == 0 else 'год не высокосный')

# Задача: проверить, является ли буква гласной
input_letter = 'g'
print('буква является гласной' if input_letter.lower() in 'aeyio' else 'буква не является гласной')

# Задача: найти корни квадратного уравнения
input_coefficients = (2, 4, 9)
a = input_coefficients[0]
b = input_coefficients[1]
c = input_coefficients[2]

d = b ** 2 - 4 * a * c

if d > 0:
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    print(f'x1 = {x1}, x2 = {x2}')
elif d == 0:
    x = -b / (2 * a)
    print(f'x = {x}')
else:
    print('нет корней')

"""
**Упражнения (Циклы):**
"""
# Задача - проверить, является ли это число простым
x = 17
list_dividers = [i for i in range(1, x + 1) if x % i == 0]
print('число является простым' if len(list_dividers) == 2 else 'число не является простым')

# Задача - найти сумму элементов главной диагонали
input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

sum = 0
for i in range(len(input_matrix)):
    sum += input_matrix[i][i]
print(f'сумма элементов главной диагонали = {sum}')

# Задача - найти количество разрядов числа
x = 100_000_000
digit = 1
x //= 10

while x > 0:
    digit += 1
    x //= 10
print(f'количество разрядов числа - {digit}')

# Задача - найти факториал числа
x = 7
d = 1
for i in range(2, x + 1):
    d *= i
print(f'факториал числа {x} = {d}')

# Задача - вывести на экран все числа, которые больше среднего значение по списку
input_list = [1, 6, 13, 76, 44, 56, 12, 13, 7, 8, 9]
s = 0
for i in input_list:
    s += i
some_list = [i for i in input_list if i > s / len(input_list)]
print(f'числа - {some_list} - ,которые больше среднего значение по списку {input_list}')

# Задача - объединить ключи и значения в словарь
keys_list = ['a', 'b', 'c', 'd', 'e']
values_list = [1, 2, 3, 4, 5]

# variant 1
some_dict = {}
index = 0
for k in keys_list:
    some_dict[k] = values_list[index]
    index += 1
print(some_dict)

# variant 2
any_some_dict = {key: value for key, value in zip(keys_list, values_list)}
print(any_some_dict)

"""
**Упражнения (Конструкторы (comprehensions)):**
"""
# Задача - создать список, содержащий все слова предложения, кроме слова "the"
input_sentence = "the quick brown fox jumps over the lazy dog"
some_list = [i for i in input_sentence.split(' ') if i != 'the']
print(some_list)

# Задача - создать словарь, в котором для всех слов кроме "the"
# ключем будет само слово, а значением количество букв, из которых оно состоит.
some_dict = {i: len(i) for i in input_sentence.split(' ') if i != 'the'}
print(some_dict)

# Задача - построить список из всех возможных комбинаций, сумма элементов которых больше 7.
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {1, 5, 9}
some_set = [(x, y, z) for x in set1 for y in set2 for z in set3 if x + y + z > 7]
print(some_set)

"""
**Упражнения (Конструкторы (comprehensions)):**
"""
# Написать функцию, которая генерирует последовательность из n чисел Фибоначчи (n принимается как аргумент).
# Воспользоваться оператором "yield"

def fib(number):
    a, b = 0, 1
    counter = 0
    while counter < number:
        yield a
        a, b = b, a + b
        counter += 1

q = fib(7)
for i in q:
    print(i)

# Написать функцию, которая проверяет, является ли строка палиндромом
def is_polidrom(str):
    for i in range(int(len(str)/2)):
        if str[i] != str[len(str) - 1 - i]:
            return False
    return True


def is_polidrom2(str):
    return str == str[::-1]


print(is_polidrom('allala'))

# Написать функцию, которая принимает неограниченное количество аргументов и возвращает максимальный четный аргумент
def get_even_number(*args):
    ret = 0
    for i in args:
        ret = ret if i < ret and i % 2 == 0 else i
    return ret


def get_even_number_2(*args):
    some_list = [i for i in args if i % 2 == 0]
    some_list.reverse()
    return some_list[0]


print(get_even_number(1, 4, 2, 7, 3, 5, 9, 10))
print(get_even_number_2(1, 4, 2, 7, 3, 5, 9, 10))

# Написать функцию, которая как аргумент принимает имя (текстом) одной из 4-х арифметических операций
# (сумма, сложение, вычитание, деление) и возвращает другую функцию, которая выполняет эту операцию для 2х переменных
def return_some_f(func, x, y):
    return func(x, y)


# Используя функцию из предыдущей задачи создать список из полученных функций (выполняющих арифметические операции)
# и применить их по очереди к одной и той же паре аргументов
def sum(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


print(return_some_f(sum, 2, 4))
print(return_some_f(sub, 2, 4))
print(return_some_f(mul, 2, 4))
print(return_some_f(div, 2, 4))

"""
**Упражнения (Элементы функционального программирования):**
"""
# Задача: создать словарь из предложенных пар ключ-значение
keys_list = [1, 2, 3, 4, 5]
values_list = ['a', 'b', 'c', 'd', 'e']
any_some_dict = {key: value for key, value in zip(keys_list, values_list)}
print(any_some_dict)

# Задача: создать список, состоящий только из палиндромов
words_tuple = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")
res = [i for i, z in zip(words_tuple, map(is_polidrom, words_tuple)) if z]
print(res)

print(list(filter(lambda x: x == x[::-1], words_tuple)))

# Задача: создать список, элементы которого равны произведениям этих списков
list1 = [1, 2, 3]
list2 = [3, 4, 5]
res = [x * y for x, y in zip(list1, list2)]
print(res)

# Задача: вывести на экран информацию о сотрудниках, принятых на работу после 2012 года и с ЗП выше 2000.
# Информация должна быть в следующем текстовом формате: "Number: 1, Dep: B, Salary: 1000, Year: 2019"
workers_table = [
    [1, 'B', 1000, 2013],
    [2, 'B', 1500, 2014],
    [3, 'B', 1800, 2012],
    [4, 'A', 2500, 2016],
    [5, 'A', 3500, 2017],
    [6, 'A', 4500, 2011],
]

some_list = list(filter(lambda x: x[2] > 2000 and x[3] > 2012, workers_table))
for i in some_list:
    print(f'Number: {i[0]}, Dep: {i[1]}, Salary: {i[2]}, Year: {i[3]}')


# Задача: добавить из второго списка в первый только те элементы, которых в нем еще нет
num_list = [1, 2, 3, 4, 5]
list_to_add = [1, 2, 3, 10, 100]
some_list = list(filter(lambda x: x not in num_list, list_to_add))
new_list = num_list + some_list
print(new_list)