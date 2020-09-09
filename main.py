from trans import *
from vectorNd import *
from matrixNd import *
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    a = Vec([1, 2])
    b = Mat([[3, 4],
             [5, 6]])
    print(a)
    print(3 * a)
    print(a + Vec([3, 4]))
    print(b)
    print("Test:")
    print(b * a)
    print(a * b)
    m = Mat([[1, 0],
             [0, 1]])
    n = Mat([[1, 2],
             [3, 4]])
    print(m[0][0])
    print(m * n)
    u = Mat.unit(2)
    print(type(u[0][1]))
    print(u)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
