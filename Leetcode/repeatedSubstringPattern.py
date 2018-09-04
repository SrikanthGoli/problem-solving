# 459. Repeated Substring Pattern


def repeatedSubstringPattern(s):
    """
    :type s: str
    :rtype: bool
    """
    str_len = len(s)
    mid = str_len//2
    helper_str = ""

    if str_len == 1:
        return True

    while mid > 0 and mid < str_len:
        if s[0:mid] in s[mid+1:]:
            mid *= 2
            print(mid, "hi")
            if mid <= str_len:
                helper_str = s[mid:]
                break
            else:
                True
        else:
            mid -= 1

    print(helper_str)
    print(str_len)

    return helper_str * (str_len//len(helper_str)) == s
