# 归并排序
def mergeSort(A: list):
    if len(A) <= 1:
        return A
    
    half = len(A) // 2
    first = mergeSort(A[:half])
    second = mergeSort(A[half:])

    i, j = 0, 0
    newA = []
    while i < len(first) or j < len(second):
        if i < len(first) and j < len(second):
            if first[i] <= second[j]:
                newA.append(first[i])
                i += 1
            else:
                newA.append(second[j])
                j += 1
        else:
            if i < len(first):
                newA.append(first[i])
                i += 1
            else:
                newA.append(second[j])
                j += 1
    return newA

A = [3, 1, 5, 6, 7, 4, 2, 8]

B = mergeSort(A)
print(B)