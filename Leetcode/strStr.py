# 28. Implement strStr()


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    i, needle_size = 0, len(needle)

    if needle_size == 0:
        return 0
    else:
        while needle_size <= len(haystack):
            if haystack[i:needle_size] == needle:
                return i
            i += 1
            needle_size += 1

    return -1
