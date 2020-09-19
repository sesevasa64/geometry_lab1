from matrix2d import *
import vector3d as v3d


class Mat3d(Mat):
    data_type = v3d.Vec3d

    def __init__(self, values: List[List[float]]):
        super().__init__(values)

    def __mul__(self, other: Union['Mat3d', 'v3d.Vec3d', float]) -> Union['Mat3d', 'v3d.Vec3d']:
        return self._mul(other)

    def __rmul__(self, other: Union['Mat3d', 'v3d.Vec3d', float]) -> Union['Mat3d', 'v3d.Vec3d']:
        return self._mul(other)

    def __truediv__(self, scalar: float):
        return self._mul(1 / scalar)

    def __add__(self, mat: 'Mat3d'):
        return self._add(mat)

    def __sub__(self, mat: 'Mat3d'):
        return self._sub(mat)

    def _mul(self, other: Union['Mat3d', float]):
        if isinstance(other, v3d.Vec3d):
            return self._mul_vector(other)
        if isinstance(other, Mat3d):
            return self._mul_matrix(other)
        if isinstance(other, Mat) and other.row() == 3:
            return self._mul_matrix(other)
        if isinstance(other, float):
            return self._mul_scalar(other)
        return NotImplemented

    @staticmethod
    def unit() -> 'Mat3d':
        return Mat3d(Mat3d._unit(3))

    @staticmethod
    def zero() -> 'Mat3d':
        return Mat3d(Mat3d._zero(3))

    @staticmethod
    def common(mat2d: 'Mat2d') -> 'Mat3d':
        res = Mat3d.unit()
        for i in range(mat2d.row()):
            for j in range(mat2d.column()):
                res[i][j] = mat2d[i][j]
        return res

    @staticmethod
    def rotate(angle: float) -> 'Mat3d':
        return Mat3d.common(Mat2d.rotate(angle))

    @staticmethod
    def parallel(k: float, _l: float) -> 'Mat3d':
        res = Mat3d.unit()
        res[0][2] = k
        res[1][2] = _l
        return res

    @staticmethod
    def scale(s: float) -> 'Mat3d':
        res = Mat3d.unit()
        res[2][2] = s
        return res

    @staticmethod
    def project(p: float, q: float) -> 'Mat3d':
        res = Mat3d.unit()
        res[2][0] = p
        res[2][1] = q
        return res

    @staticmethod
    def rotate_around_point(angle: float, k: float, _l: float) -> 'Mat3d':
        res = Mat3d.common(Mat2d.rotate(angle))
        res[0][2] = k
        res[1][2] = _l
        return res
