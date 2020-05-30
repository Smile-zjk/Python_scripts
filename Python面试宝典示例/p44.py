# 欧几里得算法求最大公约数
# 假设有两个数a和b, 且a > b, d = a % b, a 和 b的最大公约数就等于b、d的最大公约数。
def gcd(a, b):
    if a % b == 0:
        return b
    d = a % b
    return gcd(b, d)

a = 128
b = 48
print("the greatest common divisor of {0} and {1} is: {2}".format(a, b, gcd(a, b)))
