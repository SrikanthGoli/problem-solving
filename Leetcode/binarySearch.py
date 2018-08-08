
# Binary Search - (O)logn

def binarySearch(key, input, left, right):

    if right >= left:

        mid = (left+right)//2

        if input[mid] == key:
            return mid
        elif key < input[mid]:
            return binarySearch(key, input, left, mid)
        else:
            return binarySearch(key, input, mid+1, right)

    return False