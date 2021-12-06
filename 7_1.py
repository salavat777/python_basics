__author__ = 'Сафиулин Салават Тельманович'


# Задача-1: Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который
# должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        sum_matrix2 = []
        for i, j in enumerate(self.matrix):
            sum_matrix1 = []
            for k, n in enumerate(j):
                sum_matrix1.append(self.matrix[i][k] + other.matrix[i][k])
            sum_matrix2.append(sum_matrix1)
        return Matrix(sum_matrix2)

    def __str__(self):
        str1 = ''
        for i in self.matrix:
            str1 += ' '.join(map(str, i)) + '\n'
        return str1


matrix1 = Matrix([[1, 1, 1], [2, 2, 2], [10, 3, 3]])
matrix2 = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
matrix3 = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
print(matrix1)
print(matrix2)
print(matrix1 + matrix2)
print(matrix1 + matrix3 + matrix2)
