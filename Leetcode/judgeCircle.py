
# 657. Judge Route Circle

def judgeCircle(moves):
    """
    :type moves: str
    :rtype: bool
    """

    helper_dict = {"R" : 1, "L": -1, "U": 1, "D": -1}
    circle = 0

    for i in range(len(moves)):
        circle += helper_dict[moves[i]]

    if circle == 0:
        return True

    return False