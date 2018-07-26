

# 859. Buddy Strings

def buddyStrings(A, B):
    """
    :type A: str
    :type B: str
    :rtype: bool
    """

    list = []
    counter = 0

    while counter < len(A):
        if A[counter] != B[counter]:
            list.append(counter)
            counter += 1
        else:
            counter += 1

    if len(list) == 2:
        if A[list[0]] == B[list[1]] and B[list[0]] == A[list[1]]:
            return True
    elif len(set(A)) == len(set(B)):
        return True

    return False


A = "ab"
B = "ab"
print(buddyStrings(A,B))