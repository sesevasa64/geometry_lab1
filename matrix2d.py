from matrixNd import *


class Mat2d(Mat):
    def __init__(self, values: Union[List[List], Mat]):
        if isinstance(values, Mat):
            if values.size() != 2:
                raise ValueError()
            super().__init__(values.values)
        else:
            super().__init__(values)

    def __mul__(self, other) -> Union['Mat2d', 'Vector.Vec']:
        res = super().__mul__(other)
        if isinstance(res, Mat):
            return Mat2d(res)
        return res

    @staticmethod
    def unit() -> 'Mat2d':
        return Mat2d(Mat.unit(2))

    @staticmethod
    def zero() -> 'Mat2d':
        return Mat2d(Mat.zero(2))

    @staticmethod
    def rotate(angle) -> 'Mat2d':
        return Mat2d([[cos(angle),   sin(angle)],
                      [-sin(angle)], cos(angle)])

    @staticmethod
    def mirror_OY() -> 'Mat2d':
        return Mat2d([[-1, 0],
                      [0, 1]])

    @staticmethod
    def mirror_OX() -> 'Mat2d':
        return Mat2d([[1, 0],
                     [0, -1]])

    @staticmethod
    def mirror_OO() -> 'Mat2d':
        return Mat2d([[-1, 0],
                      [0, -1]])

    @staticmethod
    def mirror_45d() -> 'Mat2d':
        return Mat2d([[0, 1],
                      [1, 0]])

    @staticmethod
    def mirror_135d() -> 'Mat2d':
        return Mat2d([[0, -1],
                      [-1, 0]])

    @staticmethod
    def scale_OX(a) -> 'Mat2d':
        return Mat2d([[a, 0],
                      [0, 1]])

    @staticmethod
    def scale_OY(d) -> 'Mat2d':
        return Mat2d([[1, 0],
                      [0, d]])

    @staticmethod
    def distortion_OX(c) -> 'Mat2d':
        return Mat2d([[1, 0],
                      [c, 1]])

    @staticmethod
    def distortion_OY(b) -> 'Mat2d':
        return Mat2d([[1, b],
                      [0, 1]])