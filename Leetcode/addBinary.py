# 67. Add Binary


def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """

    i, j = len(a)-1, len(b)-1
    res = ""
    carry = 0
    while i >= 0 or j >= 0:
        s = carry
        if i >= 0 and a[i] == '1':
            s += 1
        if j >= 0 and b[j] == '1':
            s += 1
        i -= 1
        j -= 1
        res += str(s%2)
        carry = int(s//2)

    if carry:
        res += str(carry)

    return res[::-1]