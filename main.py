import numpy as np
from random import *
import matplotlib.pyplot as plt
from matrix2d import *
from vectorNd import *
from vector2d import *
from vector3d import *
from polygon import *
from figure import *

n = 4  # Номер бригады
size = n + 2  # Количество точек в многоугольнике


def line(v1: Vec2d, v2: Vec2d):
    return (v2.y - v1.y) / (v2.x - v1.x), (v2.x * v1.y - v1.x * v2.y) / (v2.x - v1.x)


def main():
    # f1()
    # f2()
    # f3_2()
    # f4()
    f5()
    # f5_2()
    pass


def f2():
    v1 = Vec2d(-1, 1)
    v2 = Vec2d(3, 2)
    (k, l) = line(v1, v2)
    print(k, l)


# Что-то вроде фрактала
def f1():
    figure = Figure()
    origin = Polygon.right(size, Vec3d(1, 0, 1))
    array = [origin]
    ln = line(origin[0], origin[1])
    array.append(origin * Mat3d.reflection_around_line(ln))
    for i in range(10):
        idx = randint(0, len(array)-1)
        p1 = randint(0, size-1)
        p2 = (p1-1) % size
        ln = line(array[idx][p1], array[idx][p2])
        for j in range(len(array)):
            array.append(array[j] * Mat3d.reflection_around_line(ln))
    figure += array
    figure.show()


# Первое задание
def f3_2():
    figure = Figure()
    origin = Polygon.right(size, Vec3d(1, 0, 1))
    array = [origin]
    var = 6
    matrix = [None,  # Отражаем относительно случайной прямой, состоящей из
                     # двух соседних точек в случайном шестиугольнике
              None,  # Отражаем относительно случайной точки с случайном шестиугольнике
              Mat3d.common(Mat2d.mirror_OO()),  # Отражаем относительно начала координат
              Mat3d.common(Mat2d.mirror_OY()),  # Отражаем относительно Oy
              Mat3d.common(Mat2d.mirror_45d()),  # Отражаем относительно y = x
              Mat3d.scale(2)]  # Уменьшаем в 2 раза
    for i in range(var):
        idx = randint(0, len(array) - 1)
        p1 = randint(0, size - 1)
        p2 = (p1 - 1) % size
        if i % var == 0:
            ln = line(array[idx][p1], array[idx][p2])
            matrix[i] = Mat3d.reflection_around_line(ln)
        if i % var == 1:
            matrix[i] = Mat3d.reflection_around_point(array[idx][p1])
        for j in range(len(array)):
            array.append(array[j] * matrix[i % var])
    figure += array
    figure.show()


# Третье задание
def f4():
    min_s = 0.1
    max_s = 5.5
    step = 0.01
    origin = Polygon.right(size, Vec3d(1, 0, 1))
    # rot = origin * Mat3d.rotate(pi/4)
    # array = [origin, rot]
    array = [origin]
    for i in np.arange(min_s, max_s, step):
        new_p = origin * Mat3d.scale(i)
        # rot = origin * Mat3d.scale(i+0.025) * Mat3d.rotate(pi/4)
        for angle in range(30, 3*30, 30):
            array.append(new_p * Mat3d.rotate(radians(angle)))
        array.append(new_p)
        # array.append(rot)
    figure = Figure()
    figure += array
    figure.show()


# Непонятно что
def f5():
    figure = Figure()
    origin = Polygon.right(size, Vec3d(1, 0, 1))#* Mat3d.parallel(Vec2d(3, 3))
    array = [origin]
    ref_mat = [Mat3d.common(Mat2d.mirror_OX()),
               Mat3d.common(Mat2d.mirror_OY())]
    for i in range(10):
        idx = randint(0, len(array)-1)
        p = randint(0, 5)
        angle = randrange(60, 360, 60)
        matrix = Mat3d.rotate_around_point((radians(angle)), array[idx][p])
        for j in range(len(array)):
            array[j] *= matrix
        for j in range(len(array)):
            array.append(array[j] * ref_mat[i % len(ref_mat)])
    figure += array
    figure.show()


# Непонятно что №2
def f5_2():
    figure = Figure()
    origin = Polygon.right(size, Vec3d(1, 0, 1))#* Mat3d.parallel(Vec2d(3, 3))
    array = [origin]
    ref_mat = [Mat3d.common(Mat2d.mirror_OX()),
               Mat3d.common(Mat2d.mirror_OY())]
    for i in range(10):
        idx = randint(0, len(array)-1)
        angle = randrange(60, 360, 60)
        center = array[idx].center()
        if center == Vec2d(0, 0):
            p1 = randint(0, 5)
            matrix = Mat3d.rotate_around_point((radians(angle)), array[idx][p1])
        else:
            matrix = Mat3d.rotate_around_point((radians(angle)), center)
        for j in range(len(array)):
            array[j] *= matrix
        for j in range(len(array)):
            array.append(array[j] * ref_mat[i % len(ref_mat)])
    figure += array
    figure.show()


if __name__ == '__main__':
    main()
