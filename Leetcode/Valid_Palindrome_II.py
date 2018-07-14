
# 680. Valid Palindrome II

def validPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """

    i, j, k = 0, len(s)-1, 0

    while i < j and k < 2:

        if s[i] != s[j] and s[i+1] == s[j]:
            if s[i+1] == s[j-1]:
                i += 1
                k += 1

        elif s[i] != s[j] and s[j-1] == s[i]:
            j -= 1
            k += 1

        elif s[i] != s[j]:
            return False

        i += 1
        j -= 1

    if k < 2:
        return True

    return False