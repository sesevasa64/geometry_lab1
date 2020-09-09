from typing import *


class Vec2d:
    def __init__(self, values: List[Any]):
        self.v = values
        self.x = self.v[0]
        self.y = self.v[1]

    def __add__(self, other: 'Vec2d'):
        return Vec2d([self.x + other.x, self.y + other.y])

    def __sub__(self, other: 'Vec2d'):
        return Vec2d([self.x - other.x, self.y - other.y])

    def __mul__(self, scalar):
        return Vec2d([self.x * scalar, self.y * scalar])

    def __truediv__(self, scalar):
        return Vec2d([self.x / scalar, self.y / scalar])
