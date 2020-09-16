import matplotlib.pyplot as plt
from vector3d import *
from matrix3d import *


class Polygon:
    def __init__(self, size: int):
        self.points = [Vec3d(0, 0, 0)] * size

    def __mul__(self, matrix: Mat3d) -> 'Polygon':
        res = Polygon(len(self.points))
        for i in range(len(self.points)):
            res[i] = self[i] * matrix
        return res
    
    def __str__(self) -> str:
        res = f"Vec()"
        for p in self.points:
            res += f"{p}\n"
        return res 

    def __getitem__(self, index: int) -> Vec3d:
        return self.points[index]

    def __setitem__(self, idx: int, value: Vec3d):
        self.points[idx] = value

    def as_xy(self):
        c = self.points.copy()  # костыль
        c.append(self[0])  # костыль
        res = [[x[0], x[1]] for x in c]  # костыль
        return zip(*res)

    @staticmethod
    def right(size: int, start: Vec3d):
        p = Polygon(size)
        p[0] = start
        rotate = Mat3d.rotate(radians(360 / size))
        for i in range(1, size):
            p[i] = p[i - 1] * rotate
        return p
