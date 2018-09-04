# 293. Flip Game


def generatePossibleNextMoves(s):
    """
    :type s: str
    :rtype: List[str]
    """
    i, j = 0, 1
    size = len(s)
    res = set()

    while i < size:
        if s[i:i+2] == '++':
            helper_str = s[:i]+"--"+s[i+2:]
            res.add(helper_str)
            i += 1
            print(helper_str)
        if j < size and s[j:j+2] == '++':
            helper_str = s[:j]+"--"+s[j+2:]
            res.add(helper_str)
            j += 1

        else:
            i += 1
            j += 1

    return list(res)
