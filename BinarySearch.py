import math


def binarySearch(arr: list, target: int) -> int:
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = math.ceil((low + high) / 2)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


arr = [1, 2, 3, 6, 8, 9, 10, 17, 20]

print(binarySearch(arr, 3))
