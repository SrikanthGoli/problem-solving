# 686. Repeated String Match

def repeatedStringMatch(A, B):
    """
    :type A: str
    :type B: str
    :rtype: int
    """
    helper = A
    count = 1

    while len(helper) <= (len(B)*2):
        if B in helper:
            return count
        else:
            helper += A
            count += 1

    if B not in helper:
        return -1

    return count