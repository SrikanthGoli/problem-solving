
# Binary Search - (O)logn
def binarySearch_recursive(key, input, left, right):

    if right >= left:

        mid = (left+right)//2

        if input[mid] == key:
            return mid
        elif key < input[mid]:
            return binarySearch_recursive(key, input, left, mid)
        else:
            return binarySearch_recursive(key, input, mid+1, right)

    return False


def binarySearch_iterative(key, input):

    left = 0
    right = len(input)-1

    while right >= left:

        mid = (left + right)//2

        if key == input[mid]:
            return mid
        elif key < input[mid]:
            right = mid-1
        elif key > input[mid]:
            left = mid+1

    return False