#125. Valid Palindrome


def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    input_lower = s.lower()
    clean_input = re.sub("[^a-z0-9]+", "", input_lower)

    i = 0
    j = len(clean_input)-1
    while i < j:
        if clean_input[i] != clean_input[j]:
            return False
        else:
            i += 1
            j -= 1

    return True
