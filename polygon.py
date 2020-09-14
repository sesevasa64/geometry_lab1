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

    def __getitem__(self, index) -> Vec2d:
        return self.points[index]

    def __setitem__(self, idx, value):
        self.points[idx] = value

    def plot(self):
        fg = plt.figure()
        sp = fg.add_subplot(111)
        copy = self.points.copy()  # костыль
        copy.append(self[0])  # костыль
        sp.plot(*zip(*copy))
        sp.axis('equal')
        return fg
