
# 13. Roman to Integer

def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    helper_dict = {'I': 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500,
                   "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

    index = 0
    total = 0

    while index < len(s):

        if s[index:index+2] in helper_dict:
            total += helper_dict[s[index:index+2]]
            index += 2

        else:
            total += helper_dict[s[index]]
            index += 1

    return total