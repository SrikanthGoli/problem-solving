def getModifiedArray(length, updates):
    """
    :type length: int
    :type updates: List[List[int]]
    :rtype: List[int]
    """
    res = [0] * length

    for triplet in updates:
        start, end, val = triplet[0], triplet[1] + 1, triplet[2]

        res[start] += val

        if end < length:
            res[end] -= val

    for i in range(1, length):
        res[i] += res[i - 1]

    return res
