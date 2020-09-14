import numpy as np
import matplotlib.pyplot as plt
from matrix2d import *
from vectorNd import *
from vector2d import *
from vector3d import *
from polygon import *


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

    #points = [start]
    #for i in range(n):
    #    points.append(points[i] * rotate)
    #points.append(start)
    #plt.plot(*zip(*points))
    plt.axis('equal')
    #plt.show()
    n = 8
    rotate = Mat2d.rotate(pi/4)
    start = Vec2d([4, 4])
    p = Polygon(n)
    p[0] = start
    for i in range(1, n):
        p[i] = p[i-1] * rotate
    f = p.plot()
    f.show()


if __name__ == '__main__':
    main()
