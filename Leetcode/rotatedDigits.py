# 788. Rotated Digits

def rotatedDigits(N):
    """
    :type N: int
    :rtype: int
    """
    x = {"0": "0", "1": "1", "8": "8", "2": "5", "5": "2", "9": "6", "6": "9"}
    res = []
    count = 0
    for i in range(N + 1):
        str_i = str(i)
        rev = ""
        for j in str_i:
            if j not in x:
                break
            else:
                rev += x[j]

        if rev != str_i and len(rev) == len(str_i):
            res.append(rev)

    return len(res)