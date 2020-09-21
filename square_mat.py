from matrixNd import *


class SquareMat(Mat):
    def __init__(self, values: List[List[float]]):
        if not SquareMat.is_square(values):
            raise ValueError()
        super().__init__(values)

    def __mul__(self, other: Union['SquareMat', Vector.Vec, float]) -> Union['SquareMat', Vector.Vec]:
        return self._mul(other)

    def __rmul__(self, other: Union['SquareMat', Vector.Vec, float]) -> Union['SquareMat', Vector.Vec]:
        return self._mul(other)

    def __truediv__(self, scalar: float):
        return self._mul(1 / scalar)

    def __add__(self, mat: 'SquareMat'):
        if not SquareMat.is_equal_size(self, mat):
            raise ValueError()
        return self._add(mat)

    def __sub__(self, mat: 'SquareMat'):
        if not SquareMat.is_equal_size(self, mat):
            raise ValueError()
        return self._sub(mat)

    def _mul(self, other: Union['SquareMat', float]):
        if isinstance(other, Vector.Vec):
            if self.size() != other.len():
                raise ValueError()
            return self._mul_vector(other)
        if isinstance(other, SquareMat):
            if not SquareMat.is_equal_size(self, other):
                raise ValueError()
            return self._mul_matrix(other)
        if isinstance(other, float):
            return self._mul_scalar(other)
        return NotImplemented

    def size(self):
        return self.row()

    def triangular(self):
        c = self.copy()
        for i in range(c.row()-1):
            index = SquareMat._not_zero_row(c, i)
            if index == -1:
                return
            (c[i], c[index]) = (c[index], c[i])
            for j in range(i+1, c.row()):
                val = -c[j][i] / c[i][i]
                row = [val * c[i][t] + c[j][t] for t in range(c.column())]
                c[j] = self._new_vec(row)
        return c

    def det(self) -> float:
        c = self.triangular()
        res = 1
        for i in range(c.row()):
            res *= c[i][i]
        return res

    def inverse(self):
        c = self.copy()
        r = SquareMat.unit(c.row())
        for i in range(c.row()):
            index = SquareMat._not_zero_row(c, i)
            if index == -1:
                return
            (c[i], c[index]) = (c[index], c[i])
            (r[i], r[index]) = (r[index], r[i])
            tmp = c[i][i]
            c[i] /= tmp
            r[i] /= tmp
            j = (i + 1) % c.row()
            while j != i:
                tmp = c[j][i]
                c[j] -= c[i] * float(tmp)
                r[j] -= r[i] * float(tmp)
                j = (j + 1) % c.row()
        return r

    @staticmethod
    def _zero(size):
        res = []
        for i in range(size):
            res.append([])
            for j in range(size):
                res[i].append(0)
        return res

    @staticmethod
    def _unit(size):
        res = SquareMat._zero(size)
        for i in range(size):
            res[i][i] = 1
        return res

    @staticmethod
    def _not_zero_row(mat: 'Mat', idx: int) -> int:
        for k in range(idx, mat.row()):
            if mat[k][idx] != 0:
                return k
        return -1

    @staticmethod
    def unit(size) -> 'Mat':
        return Mat(SquareMat._unit(size))

    @staticmethod
    def zero(size) -> 'Mat':
        return Mat(SquareMat._zero(size))

    @staticmethod
    def is_square(values: List[List[float]]):
        for val in values:
            if len(val) != len(values):
                return False
        return True

    @staticmethod
    def is_equal_size(mat1: 'SquareMat', mat2: 'SquareMat'):
        return mat1.size() == mat2.size()

    @staticmethod
    def is_Nd(values: List[List[float]], n: int):
        if len(values) == n:
            for val in values:
                if len(val) != n:
                    return False
            return True
        return False
