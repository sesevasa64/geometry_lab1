import numpy as np
import matplotlib.pyplot as plt
from matrix2d import *
from vectorNd import *
from vector2d import *
from vector3d import *
from polygon import *
from figure import *


def main():
    a = Vec([1, 2])
    b = Mat([[3, 4],
             [5, 6]])
    print(a)
    print(3 * a)
    print(a + Vec([3, 4]))
    print(b)
    print("Test:")
    print(b * a)
    print(a * b)
    m = Mat([[1, 0],
             [0, 1]])
    n = Mat([[1, 2],
             [3, 4]])
    print(m[0][0])
    print(m * n)
    u = Mat.unit(2)
    print(type(u[0][1]))
    print(u)

    d2 = Mat2d.unit()
    r2 = d2 * m
    print(type(r2))

    # points = [start]
    # for i in range(n):
    #    points.append(points[i] * rotate)
    # points.append(start)
    # plt.plot(*zip(*points))
    plt.axis('equal')
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
    fig = Figure()
    p1 = Polygon.right(8, Vec3d([4, 4, 1]))
    fig += p1
    fig.show()


if __name__ == '__main__':
    main()
