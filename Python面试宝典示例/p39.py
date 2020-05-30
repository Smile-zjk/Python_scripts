def closestWithTheSameWeight(x):
    # 假设x是64位数
    for i in range(64):
        if ((x >> i) & 1) ^ ((x >> (i+1)) & 1):
            # 交换两个相邻的比特位
            x ^= (1 << i) | (1 << (i+1))
            return x

x = 0b11011
y = closestWithTheSameWeight(x)
print("integer closest to x with the same weight is {0}".format(bin(y)))