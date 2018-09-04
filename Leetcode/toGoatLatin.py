# 824. Goat Latin


def toGoatLatin(S):
    """
    :type S: str
    :rtype: str
    """
    output = ""
    count = 1
    arb_list = ['a', 'e', 'i', 'o', 'u']
    words = S.split()

    for i in words:
        if i[0].lower() in arb_list:
            if len(words) != count:
                output += i+ "ma" + ("a" * count) + " "
                count += 1
            else:
                output += i + "ma" + ("a" * count)
        elif i[0].lower() not in arb_list:
            if len(words) != count:
                output += i[1:] + i[0] + "ma" + ("a" * count) + " "
                count += 1
            else:
                output += i[1:] + i[0] + "ma" + ("a" * count)

    return output
