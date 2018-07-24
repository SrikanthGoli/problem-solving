# 67. Add Binary

def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """

    i, j = len(a)-1, len(b)-1
    count = 0
    res = ""

    while i >= 0 and j >= 0:
        if a[i] + b[j] + count == 2:
            count = 1
            res += '0'
            i -= 1
            j -= 1
        elif a[i] + b[j] + count == 3:
            count = 1
            res += '1'
            i -= 1
            j -= 1
        elif a[i] + b[j] + count == 1:
            count = 0
            res += '1'
            i -= 1
            j -= 1
        else:
            count = 0
            res += '0'
            j -= 1
            i -= 1

    while i >= 0:

