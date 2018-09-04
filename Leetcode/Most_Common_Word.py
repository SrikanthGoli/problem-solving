# 819. Most Common Word


def mostCommonWord(paragraph, banned):
    """
    :type paragraph: str
    :type banned: List[str]
    :rtype: str
    """

    input_lower = [l.lower().strip("!?',;.") for l in paragraph.split()]
    helper_dict = {}

    for i in input_lower:
        if i not in banned and i not in helper_dict:
            helper_dict[i] = 1

        elif i not in banned:
            helper_dict[i] += 1

    output = max(helper_dict, key = helper_dict.get)

    return output
