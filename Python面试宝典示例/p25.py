# 二分排序
def binaryFind(A: list, m: int) -> int:  
    low = 0
    high = len(A) - 1
    mid = (low + high) // 2
    while low <= high:
        if A[mid] == m:
            return mid
        elif A[mid] > m:
            high = mid - 1
            mid = (low + high) // 2 
        elif A[mid] < m:
            low = mid + 1
            mid = (low + high) // 2
    return -1

A = [3, 1, 5, 6, 7, 4, 2, 8]
A.sort()
M = 9
success = False
for i in range(len(A)):1
    m = M - A[i]
    j = binaryFind(A, m)
    if j != -1 and j != i:
        print("存在i和j,使得A[i] + A[j] = {0}".format(M))
        success = True
        break
if not success:
    print("不存在i和j,使得A[i] + A[j] = {0}".format(M))