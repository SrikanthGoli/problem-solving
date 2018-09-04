# 387. First Unique Character in a String


def firstUniqChar(s):
    """
    :type s: str
    :rtype: int
    """

    aux_dict = {}
    count = 0

    for i in s:
        if i not in aux_dict:
            aux_dict[i] = 1
        else:
            aux_dict[i] += 1

    for i in s:
        if aux_dict[i] == 1:
            return count
        count += 1

    return -1
