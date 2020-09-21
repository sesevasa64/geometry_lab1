from matrix2d import *
import vector3d as v3d


class Mat3d(SquareMat):
    data_type = v3d.Vec3d

    def __init__(self, values: List[List[float]]):
        if not Mat2d.is_Nd(values, 3):
            raise ValueError()
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
        return Mat3d(SquareMat._unit(3))

    @staticmethod
    def zero() -> 'Mat3d':
        return Mat3d(SquareMat._zero(3))

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
    def parallel(point: Vec2d) -> 'Mat3d':
        res = Mat3d.unit()
        res[2][0] = point[0]
        res[2][1] = point[1]
        return res

    @staticmethod
    def scale(s: float) -> 'Mat3d':
        res = Mat3d.unit()
        res[2][2] = s
        return res

    @staticmethod
    def project(point: Vec2d) -> 'Mat3d':
        res = Mat3d.unit()
        res[2][0] = point[0]
        res[2][1] = point[1]
        return res

    @staticmethod
    def rotate_around_point(angle: float, point: Vec2d) -> 'Mat3d':
        res = Mat3d.common(Mat2d.rotate(angle))
        k = point[0] * (1 - cos(angle)) + point[1] * sin(angle)
        _l = point[1] * (1 - cos(angle)) - point[0] * sin(angle)
        res[2][0] = k
        res[2][1] = _l
        return res

    @staticmethod
    def reflection_around_line(line: Tuple[float, float]):
        (k, l) = line
        a = 2 * -atan(k)
        return Mat3d([[cos(a),   -sin(a),      0],
                      [-sin(a),  -cos(a),      0],
                      [l*sin(a), l*(1+cos(a)), 1]])



