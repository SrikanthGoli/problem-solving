def maxScoreSightseeingPair(A):
    """
    :type A: List[int]
    :rtype: int
    """
    res, curr = 0, 0

    for sight in A:
        res = max(res, sight + curr)
        curr = max(curr, sight) - 1

    return res
