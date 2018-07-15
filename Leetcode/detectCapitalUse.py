
# 520. Detect Capital

def detectCapitalUse(word):

    """
    :type word: str
    :rtype: bool
    """

    size = len(word)
    upper_count = 0
    lower_count = 0

    for i in range(0, len(word)):

        if ord(word[i]) < 97:
            upper_count += 1
        else:
            lower_count += 1

    if upper_count == size or (upper_count == 1 and word[0].isupper()) or lower_count ==size:
        return True

    return False