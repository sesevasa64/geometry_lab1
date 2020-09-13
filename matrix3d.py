from matrix2d import *
from vector3d import *


class Mat3d(Mat):
    def __init__(self, values: Union[List[List], Mat]):
        if isinstance(values, Mat):
            if values.size() != 3:
                raise ValueError()
            values = values.values
        super().__init__(values)

    def __mul__(self, other) -> Union['Mat3d', 'Vec3d']:
        res = super().__mul__(other)
        if isinstance(res, Mat):
            return Mat3d(res)
        return Vec3d(res)

    @staticmethod
    def unit(size=3) -> 'Mat3d':
        return Mat3d(Mat.unit(3))

    @staticmethod
    def zero(size=3) -> 'Mat3d':
        return Mat3d(Mat.zero(3))

    @staticmethod
    def common(mat2d: 'Mat2d') -> 'Mat3d':
        res = Mat3d.unit()
        for i in range(mat2d.row()):
            for j in range(mat2d.column()):
                res[i][j] = mat2d[i][j]
        return res

    @staticmethod
    def parallel(k, _l) -> 'Mat3d':
        res = Mat3d.unit()
        res[0][2] = k
        res[1][2] = _l
        return res

    @staticmethod
    def scale(s) -> 'Mat3d':
        res = Mat3d.unit()
        res[2][2] = s
        return res

    @staticmethod
    def project(p, q) -> 'Mat3d':
        res = Mat3d.unit()
        res[2][0] = p
        res[2][1] = q
        return res
