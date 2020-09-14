import matplotlib.pyplot as plt
from vector2d import *
from matrix2d import *


class Polygon:
    def __init__(self, size: int):
        self.points = [Vec2d([0, 0])] * size

    def __mul__(self, matrix: Mat2d) -> 'Polygon':
        res = Polygon(len(self.points))
        for i in range(len(self.points)):
            res[i] = self[i] * matrix
        return res

    def __getitem__(self, index: int) -> Vec2d:
        return self.points[index]

    def __setitem__(self, idx: int, value: Vec2d):
        self.points[idx] = value

    def plot(self):
        fg = plt.figure()
        sp = fg.add_subplot(111)
        copy = self.points.copy()  # костыль
        copy.append(self[0])  # костыль
        sp.plot(*zip(*copy))
        sp.axis('equal')
        return fg

    @staticmethod
    def right(size: int, start: Vec2d):
        p = Polygon(size)
        p[0] = start
        rotate = Mat2d.rotate(radians(360 / size))
        for i in range(1, size):
            p[i] = p[i - 1] * rotate
        return p
