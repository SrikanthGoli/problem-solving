def shortestWordDistance(words, word1, word2):
    """
    :type words: List[str]
    :type word1: str
    :type word2: str
    :rtype: int
    """
    res, l1, l2 = float('inf'), float('inf'), float('inf')

    flag = True if word1 == word2 else False

    for i in range(len(words)):

        if words[i] == word1:
            if flag:
                l1 = l2
                l2 = i
            else:
                l1 = i
        elif words[i] == word2:
            l2 = i

        res = min(res, abs(l2 - l1))

    return res