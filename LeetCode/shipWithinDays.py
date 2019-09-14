def shipWithinDays(weights, D):
    """
    :type weights: List[int]
    :type D: int
    :rtype: int
    """
    low, high = max(weights), sum(weights)

    while low < high:
        need, curr = 1, 0
        mid = low + (high - low) // 2

        for i in weights:
            if curr + i > mid:
                need += 1
                curr = 0
            curr += i

        if need > D:
            low = mid + 1
        else:
            high = mid

    return low
