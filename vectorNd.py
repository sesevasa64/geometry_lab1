from typing import *


class Vec:
    def __init__(self, *args):
        self.values = list(args)

    def __str__(self) -> str:
        return f"Vec{self._format()}"

    def __add__(self, other: 'Vec') -> 'Vec':
        return self._add(other)

    def __sub__(self, other: 'Vec') -> 'Vec':
        return self._sub(other)

    def __mul__(self, other: float) -> 'Vec':
        if isinstance(other, float):
            return self._mul_scalar(other)
        return NotImplemented

    def __rmul__(self, other: float) -> 'Vec':
        return self._mul_scalar(other)

    def __truediv__(self, scalar: float) -> 'Vec':
        return self._div_scalar(scalar)

    def __eq__(self, other: 'Vec'):
        return self._eq(other)

    def __getitem__(self, index: int) -> float:
        return self.values[index]

    def __setitem__(self, index: int, value: float):
        self.values[index] = value

    def __iter__(self):
        for val in self.values:
            yield val

    def len(self) -> int:
        return len(self.values)

    def normie(self) -> 'Vec':
        return self / self[-1]

    def _format(self):
        return [round(x, 2) for x in self.values]

    def _add(self, other):
        return self.from_list([v1 + v2 for (v1, v2) in zip(self.values, other.values)])

    def _sub(self, other: 'Vec'):
        return self.from_list([v1 - v2 for (v1, v2) in zip(self.values, other.values)])

    def _div_scalar(self, scalar: float):
        return self.from_list([val / scalar for val in self.values])

    def _mul_scalar(self, scalar: float):
        return self.from_list([val * scalar for val in self.values])

    def _eq(self, other):
        eps = 0.001
        for i in range(len(self.values)):
            if not abs(self[i] - other[i]) < eps:
                return False
        return True

    @classmethod
    def from_list(cls, values: List[float]):
        vec = cls()
        vec.values = values
        return vec
