import numpy as np
import matplotlib.pyplot as plt
from matrix2d import *
from vectorNd import *
from vector2d import *
from vector3d import *
from polygon import *
from figure import *


def main():
    a = Vec(1, 2)
    b = Mat([[3, 4],
             [5, 6]])
    print(a)
    print(3 * a)
    print(a + Vec(3, 4))
    print(b)
    print(f"b * a = {b * a}")
    print(f"a * b = {a * b}")
    m = Mat([[1, 0],
             [0, 1]])
    n = Mat([[1, 2],
             [3, 4]])
    print(f"m * n = {m * n}")
    u = Mat.unit(2)
    print(f'Unit(2x2) = {u}')

    d2 = Mat2d.unit()
    print(f"d2 = {d2}")
    r2 = d2 * m
    print(f'd2 * m = {r2}')

    p = Polygon.right(5, Vec3d(4, 4, 1))

    f = Figure()
    f += p
    f.show()
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

    # tri = Mat3d([[2, 1, 4],
    #              [7, 2, 3],
    #              [7, 5, 5]])
    # print(tri.triangular())
    # print(tri.det())
    # print(tri.inverse())

    # v = Vec2d(1, 2)
    # v2 = v/5
    # print(type(v2))


def foo():
    class A:
        def __init__(self, a):
            self.a = a

        def method(self, a):
            return self.__class__(a)

    class B(A):
        pass

    b = B(5)
    c = b.method(10)
    print(type(c))
    print(c.a)


if __name__ == '__main__':
    main()
    # foo()
