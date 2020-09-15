import matplotlib.pyplot as plt
from polygon import *


class Figure:
    def __init__(self):
        self.fig = plt.figure()
        self.sp = self.fig.add_subplot(111)
        self.sp.axis('equal')
        self.poly: List[Polygon] = []

    def __iadd__(self, other: Polygon):
        self.poly.append(other)
        return self

    def __isub__(self, other: Polygon):
        self.poly.remove(other)

    def remove(self, idx: int):
        self.poly.pop(idx)

    def plot(self):
        for p in self.poly:
            self.sp.plot(*p.as_xy())

    def show(self):
        self.plot()
        self.fig.show()

    def save_fig(self):
        self.plot()
        self.fig.savefig()

    def __getitem__(self, index: int) -> Polygon:
        return self.poly[index]

    def __setitem__(self, idx: int, value: Polygon):
        self.poly[idx] = value
