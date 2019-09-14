def pancakeSort(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    res = []

    for m in range(len(A), 1, -1):
        i = A.index(m)
        res += [i + 1, m]
        A = A[:i:-1] + A[:i]

    return res