# 383. Ransom Note


def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """

    aux_dict = {}

    for i in magazine:
        if i not in aux_dict:
            aux_dict[i] = 1
        else:
            aux_dict[i] += 1

    for i in ransomNote:
        if i in aux_dict and aux_dict[i] > 0:
            aux_dict[i] -= 1

        else:
            return False

    return True