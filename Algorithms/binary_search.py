def binary_search(sorted_list: list, item: int):
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_list[mid] == item:
            return mid
        elif sorted_list[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]

assert binary_search(my_list, 3) == 1
assert binary_search(my_list, -1) == None
