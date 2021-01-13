from functools import reduce
from math import gcd


def getTotalX(a, b):
    # Find the GCD array B
    lcm_a = reduce(lambda x, y: x * y // gcd(x, y), a)
    # Find the LCM array A
    gcd_b = reduce(gcd, b)
    # Count the number of multiples of LCM that evenly divides the GCD.
    return sum([1 for num in range(lcm_a, gcd_b + 1, lcm_a) if gcd_b % num == 0])


if __name__ == '__main__':
    input()  # We don't need the first input
    arr = list(map(int, input().strip().split()))
    brr = list(map(int, input().strip().split()))
    total = getTotalX(arr, brr)
    print(total)
