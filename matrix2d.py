from math import *
from vector2d import *


class Mat2d:
    def __init__(self, values: List[List[Any, Any], List[Any, Any]]):
        self.v = values
        (self.a, self.b) = (self.v[0][0], self.v[0][1])
        (self.c, self.d) = (self.v[1][0], self.v[1][1])

    def __mul__(self, vec: 'Vec2d'):
        return Vec2d([self.a * vec.x + self.c * vec.y,
                      self.b * vec.x + self.d * vec.y])

    @staticmethod
    def rotate(angle: float):
        return Mat2d([[cos(angle),   sin(angle)],
                      [-sin(angle)], cos(angle)])


a = Vec2d([1, 2])
b = Mat2d([[1, 2],
           [3, 4]])
