"""
Упражнения (использовать только матричные операции)
"""
import numpy as np

v = np.array([1, 2, 3, 4, 5, 6])
# Получить сумму элементов и сумму квадратов элементов вектора:
print(np.sum(v))
print(np.sum(v ** 2))

# Для вектора из предыдущей задачи построить вектор, каждым элементом которого является среднее значение вектора.
print([np.average(v)] * 6)

# Написать функцию, которая принимает на вход произвольное количество матриц,
# проверяет можно ли их перемножить, и если можно, то возвращает размерность результата.
def get_shape_matrix(*args):
    for i in args:
        a = np.array(i)
    matrix = a.dot(a)
    return matrix.shape

# Вычислить выражение:
# ∑𝑖=1𝑛(𝑥𝑖−𝑎𝑣𝑔(𝑥))2

# Вывести матрицу, которая при умножении на вектор слева приводит его к форме отклонения от среднего значения.
# То есть каждым элементом вектора-результата будет соответствующий элемент входящего вектора минус среднее значение.

# Решить систему уравнений:
# 47𝑎2+71𝑏−2𝑐=3
# 11𝑏−8𝑐=3
# 𝑎2+𝑏+𝑐=24
y = np.array([3, 3, 24])
A = np.array([
    [47, 71, -2],
    [0, 11, -8],
    [1, 1, 1]
])
x = np.linalg.solve(A, y)
a, b, c = x
print(47/(a ** 0.5), b, c)

# print(47 * ((a ** 0.5) ** 2) + 71 * b - 2 * c)
# print(11 * b - 8 * c)
# print(((a ** 0.5) ** 2) + b + c)
