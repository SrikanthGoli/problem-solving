# 408. Valid Word Abbreviation

def validWordAbbreviation(word, abbr):
    """
    :type word: str
    :type abbr: str
    :rtype: bool
    """

    i, j = 0, 0
    word_len, abb_len = len(word), len(abbr)

    while i < word_len and j < abb_len:
        if word[i] == abbr[j]:
            i += 1
            j += 1
        elif abbr[j] == "0":
            return False
        elif abbr[j].isnumeric():
            k = ""
            while j < abb_len and abbr[j].isnumeric():
                k += abbr[j]
                j += 1
            i += int(k)
        else:
            return False

    return j == abb_len and i == word_len