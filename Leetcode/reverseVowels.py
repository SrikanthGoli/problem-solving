# 345. Reverse Vowels of a String

def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """

    i, j = 0, len(s)-1
    vowels = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
    helper_list = list(s)

    while i < j:
        if helper_list[i] in vowels and helper_list[j] in vowels:
            helper_list[i], helper_list[j] = helper_list[j], helper_list[i]
            i += 1
            j -= 1
        elif helper_list[i] in vowels:
            j -= 1
        elif helper_list[j] in vowels:
            i += 1
        else:
            i += 1
            j -= 1

    return "".join(helper_list)