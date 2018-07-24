# 67. Add Binary

def addBinary(a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """

    i, j = len(a)-1, len(b)-1
    carry = 0
    res = ""

    while i >= 0 and j >= 0:
        if int(a[i]) + int(b[j]) + carry == 2:
            carry = 1
            res += '0'
        elif int(a[i]) + int(b[j]) + carry == 3:
            carry = 1
            res += '1'
        elif int(a[i]) + int(b[j]) + carry == 1:
            carry = 0
            res += '1'
        else:
            carry = 0
            res += '0'
        i -= 1
        j -= 1

    while i >= 0:
        if int(a[i]) + carry == 2:
            carry = 1
            res += '0'
        elif int(a[i]) + carry == 1:
            carry = 0
            res += '1'
        else:
            carry = 0
            res += '0'
        i -= 1

    while j >= 0:
        if int(b[j]) + carry == 2:
            carry = 1
            res += '0'
        elif int(b[j]) + carry == 1:
            carry = 0
            res += '1'
        else:
            carry = 0
            res += '0'
        j -= 1

    if carry > 0:
        res += str(carry)

    return res[::-1]