import matplotlib.pyplot as plt
from vector3d import *
from matrix3d import *


class Polygon:
    def __init__(self, size: int):
        self.points = [Vec3d()] * size

    def __mul__(self, matrix: Mat3d) -> 'Polygon':
        res = Polygon(len(self.points))
        for i in range(len(self.points)):
            res[i] = self[i] * matrix
        return res
    
    def __str__(self) -> str:
        res = f"Poly\n"
        for p in self.points:
            res += f"{p}\n"
        return res 

    def __getitem__(self, index: int) -> Vec3d:
        return self.points[index]

    def __setitem__(self, idx: int, value: Vec3d):
        self.points[idx] = value

    def __iter__(self):
        for point in self.points:
            yield point

    def center(self):
        a_sum, c_sum_x, c_sum_y = 0, 0, 0
        size = len(self.points)
        for i in range(size):
            ip1 = (i + 1) % size
            a_sum += self[i].x * self[ip1].y - self[ip1].x * self[i].y
            c_sum_x += (self[i].x + self[ip1].x) * \
                       (self[i].x * self[ip1].y - self[ip1].x * self[i].y)
            c_sum_y += (self[i].y + self[ip1].y) * \
                       (self[i].x * self[ip1].y - self[ip1].x * self[i].y)
        k = 3 * a_sum
        c_x = c_sum_x / k
        c_y = c_sum_y / k
        return Vec2d(c_x, c_y)

    def area(self):
        res = 0
        size = len(self.points)
        for i in range(size):
            ip1 = (i + 1) % size
            res += self[i].x * self[ip1].y - self[ip1].x * self[i].y
        return res

    def as_xy(self):
        c = self.points.copy()  # костыль
        c.append(self[0])  # костыль
        res = [[point.x / point.z, point.y / point.z] for point in c]  # костыль
        return zip(*res)

    @staticmethod
    def right(size: int, start: Vec3d):
        p = Polygon(size)
        p[0] = start
        rotate = Mat3d.rotate(radians(360 / size))
        for i in range(1, size):
            p[i] = p[i - 1] * rotate
        return p
