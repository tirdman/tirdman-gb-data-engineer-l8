"""
Задание 1.

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return "\n".join([" ".join(map(lambda a: str(a), item)) for item in self.matrix])

    #
    def __add__(self, other):
        new_list = []
        for i in range(0, len(self.matrix)):
            new_list.append([self.matrix[i][j] + other.matrix[i][j] for j in range(0, len(self.matrix[i]))])
        return Matrix(new_list)


matrix_a = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_b = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(f'Вывод матрицы А:')
print(matrix_a)
print()

print(f'Вывод матрицы B:')
print(matrix_b)
print()

matrix_c = matrix_a + matrix_b
print(f'Вывод матрицы C:')
print(matrix_c)
