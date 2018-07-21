
#14. Longest Common Prefix

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    input_len = len(strs)

    if input_len < 1:
        return ""

    else:
        strs.sort(key=len)
        key, i = strs[0], 1

        while i > 0 and i < input_len:
            k = len(key)
            if strs[i][:k] != key:
                key = key[:-1]
                i -= 1
            i += 1

    return key