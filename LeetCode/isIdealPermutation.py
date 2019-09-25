def isIdealPermutation(A):
    """
    :type A: List[int]
    :rtype: bool
    """

    m, N = float('inf'), len(A)

    for i in range(N - 1, -1, -1):
        m = min(m, A[i])
        if i >= 2 and A[i - 2] > m:
            return False

    return True
