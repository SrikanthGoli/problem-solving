def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    res = [[0 for x in range(n)] for x in range(n)]
    counter = 1

    r1, r2 = 0, n - 1
    c1, c2 = 0, n - 1

    def coordinates(r1, r2, c1, c2):
        for c in range(c1, c2 + 1):
            yield r1, c
        for r in range(r1 + 1, r2 + 1):
            yield r, c2
        if r1 < r2 and c1 < c2:
            for c in range(c2 - 1, c1, -1):
                yield r2, c
            for r in range(r2, r1, -1):
                yield r, c1

    while r1 <= r2 and c1 <= c2:
        for r, c in coordinates(r1, r2, c1, c2):
            res[r][c] = counter
            counter += 1

        r1 += 1; c1 += 1
        r2 -= 1; c2 -= 1

    return res