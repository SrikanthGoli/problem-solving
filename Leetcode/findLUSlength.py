
# 521. Longest Uncommon Subsequence I

def findLUSlength(a, b):
    """
    :type a: str
    :type b: str
    :rtype: int
    """
    if a == b:
        return -1

    elif len(a) >= len(b):
        return len(a)

    return len(b)