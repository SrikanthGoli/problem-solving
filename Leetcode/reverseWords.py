# 557. Reverse Words in a String III


def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    output = ""
    for i in s.split():
        if len(output) == 0:
            output += i[::-1]
        else:
            output += " "+i[::-1]

    return output
