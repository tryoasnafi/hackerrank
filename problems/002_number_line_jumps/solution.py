# Look at to the case:
# https://www.hackerrank.com/challenges/kangaroo/problem

"""
Formula:
Kangaroo Position = (Number of jumps * Distance per Jump) + Starting Position

The equation is:
K = y * v + x

We must find the number of jumps each kangaroo (y)

Because we have 2 kangaroo, now the equation like:
(y * v1) + x1 = (y * v2) + x2
(y * v1) - (y * v2) = x2 - x1
y (v1 - v2) = x2 - x1
y = (x2 - x1) / (v1 - v2)

So, to find the number of jumps we must use the equation = (x2 - x1) / (v1 - v2)
"""

# Complete the kangaroo function below.


def kangaroo(x1, v1, x2, v2):
    # We have to make sure `Kangaroo 2` slower than `Kangaroo 1`
    # because Starting Location of `Kangaroo 2` is ahead,
    # that mean `Kangaroo 2` can't same or faster than `Kangaroo 1`
    # or `Kangaroo 1` will never catch up and can't intersect each other.

    # if (v2 < v1):
    #     if ((x2 - x1) % (v1 - v2) == 0):
    #         return 'YES'

    # Refactoring (one line solution)
    return 'YES' if (v2 < v1) and (x2 - x1) % (v1 - v2) == 0 else 'NO'


if __name__ == '__main__':
    x1V1X2V2 = input().split()
    data = list(map(int, x1V1X2V2))
    result = kangaroo(data[0], data[1], data[2], data[3])
    print(result)
