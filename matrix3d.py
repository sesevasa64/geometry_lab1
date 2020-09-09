from math import *
from vector2d import *


class Mat3d:
    def __init__(self, values: List[List[Any, Any, Any], List[Any, Any, Any], List[Any, Any, Any]]):
        self.v = values
        (self.a, self.b, self.p) = (self.v[0][0], self.v[0][1], self.v[0][2])
        (self.c, self.d, self.q) = (self.v[1][0], self.v[1][1], self.v[1][2])
        (self.k, self.l, self.s) = (self.v[2][0], self.v[2][1], self.v[2][2])

    def __mul__(self, vec: 'Vec2d'):
        return Vec2d([self.a * vec.x + self.c * vec.y,
                      self.b * vec.x + self.d * vec.y])

    @staticmethod
    def rotate(angle: float):
        return Mat3d([[cos(angle),   sin(angle)],
                      [-sin(angle)], cos(angle)])