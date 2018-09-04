# 804. Unique Morse Code Words


def uniqueMorseRepresentations(words):
    """
    :type words: List[str]
    :rtype: int
    """
    morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

    helper_set = set()

    for i in words:
        helper_str = ""
        for j in range(len(i)):
            helper_str += morse[ord(i[j]) - ord('a')]

        helper_set.add(helper_str)

    return len(helper_set)
