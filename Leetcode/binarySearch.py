
# Binary Search - (O)logn

def binarySearch(key, input, left, right):

    if left > right:
        return False

    mid = (left+right)//2

    if key == input[mid]:
        return mid
    elif key < input[mid]:
        binarySearch(key, input, left, mid)
    else:
        binarySearch(key, input, mid+1, right)

    return None


test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 14]
print(binarySearch(9, test, 0, 11))