def binarySearch(arr, element, start=0, end=-1) -> int:
    """
        Search Using recursion
        Input --> Sorted(Array),element to search
        Return --> Index of Element
    """
    if end == -1:
        end = len(arr) - 1
    mid = (start + end) // 2
    if element == arr[mid]:
        return mid
    if mid == end:
        return -1
    else:
        if element > arr[mid]:
            return binarySearch(arr, element, mid + 1, end)
        else:
            return binarySearch(arr, element, start, mid - 1)


if __name__ == "__main__":
    pass
    # index = binarySearch([-3, 1, 5, 9, 17, 18, 20], 17)
    # print(index)
