import numpy as np
import matplotlib.pyplot as plt
from matrix2d import *
from vectorNd import *
from vector2d import *
from vector3d import *
from polygon import *
from figure import *


def line(v1: Vec2d, v2: Vec2d):
    return (v2.y - v1.y) / (v2.x - v1.x), (v2.x * v1.y - v1.x * v2.y) / (v2.x - v1.x)


def main():
    f1()
    f2()


def f2():
    v1 = Vec2d(-1, 1)
    v2 = Vec2d(3, 2)
    (k, l) = line(v1, v2)
    print(k, l)


def f1():
    n = 4
    size = n + 2
    figure = Figure()
    angle = radians(360/size)
    origin = Polygon.right(size, Vec3d(1, 0, 1))
    array = []
    #for i in range(1, 7):
    #    poly = origin * Mat3d.parallel(2. * origin[i-1].to2d())
    #    poly *= Mat3d.rotate_around_point(angle, origin[i-1].to2d())
    #    array.append(poly)
    #for i in range(1, 8):
    #    for j in range(1, 7):
    #        #poly = array[i-1] * Mat3d.parallel(2. * array[i-1][j-1].to2d())
    #        #poly *= Mat3d.rotate_around_point(angle, array[i-1][j-1].to2d())
    #        poly = array[i-1] * Mat3d.rotate_around_point(angle, array[i-1][j-1].to2d())
    #        array.append(poly)
    for i in range(1, 7):
        ln = line(origin[i-1], origin[i % 6])
        r = origin * Mat3d.reflection_around_line(ln)
        array.append(r)
    figure += origin
    figure += array
    figure.show()


if __name__ == '__main__':
    main()

    # a = Vec(1, 2)
    # b = Mat([[3, 4],
    #          [5, 6]])
    # print(f"a = {a}")
    # print(f"3 * a = {3 * a}")
    # print(f"a + Vec(3, 4) = {a + Vec(3, 4)}")
    # print(f"b = {b}")
    # print(f"b * a = {b * a}")
    # print(f"a * b = {a * b}")
    # m = Mat([[1, 0],
    #          [0, 1]])
    # n = Mat([[1, 2],
    #          [3, 4]])
    # print(f"m = {n}")
    # print(f"m = {m}")
    # print(f"m * n = {m * n}")
    # u = SquareMat.unit(2)
    # print(f'Unit(2x2) = {u}')

    # d2 = Mat2d.unit()
    # print(f"d2 = {d2}")
    # r2 = d2 * m
    # print(type(d2))
    # print(type(r2))
    # print(f'd2 * m = {r2}')

    # p = Polygon.right(6, Vec3d(4, 4, 1))

    # f = Figure()
    # f += p
    # f.show()
    # points = [start]
    # for i in range(n):
    #    points.append(points[i] * rotate)
    # points.append(start)
    # plt.plot(*zip(*points))
    # plt.axis('equal')
    # plt.show()
    # n = 8
    # rotate = Mat2d.rotate(radians(360/n))
    # start = Vec2d([4, 4])
    # p = Polygon(n)
    # p[0] = start
    # for i in range(1, n):
    #    p[i] = p[i-1] * rotate
    # f = p.plot()
    # f.show()
    # f = plt.figure()
    # sp = f.add_subplot(111)
    # p = Polygon.right(8, Vec3d([4, 4, 0]))
    # p.plot(sp)
    # v3d = Vec3d([1, 1, 0])
    # p1 = Polygon.right(8, Vec3d([2, 2, 1]))
    # for i in range(20):
    #    for j in range(10):
    #        dp = Mat3d.project(i, j)
    #        (p1 * dp).plot(sp)
    #        dp = Mat3d.scale(36)
    #        (p1 * dp).plot(sp)
    # f.savefig("foo.png")
    # f.show()
    # fig = Figure()
    # p1 = Polygon.right(8, Vec3d(4, 4, 1))
    # fig += p1
    # fig.show()

    # tri = Mat3d([[2, 2, 3],
    #              [2, 2, 4],
    #              [5, 6, 7]])
    # print(tri.triangular())
    # print(tri.det())
    # print(tri.inverse())
    # print(tri * tri.inverse())

    # res = Mat([])
    # res.values = [Vec()]*4
    # res[0] = Vec(1)
    # print(res)
    # m1 = SquareMat.unit(2)
    # print(m1)
    # m2 = m1.copy()
    # m1[0][0] = 2
    # print(m1)
    # print(m2)

    # v = Vec2d(1, 2)
    # v2 = v/5
    # print(type(v2))
    # print(Mat.data_type)
    # print(Mat2d.data_type)
    # print(Mat3d.data_type)
    # print(Mat.data_type)
