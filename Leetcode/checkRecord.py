
#551. Student Attendance Record I

def checkRecord(s):
    """
    :type s: str
    :rtype: bool
    """
    count = 0
    size = len(s)

    for i in range(size):
        if s[i] == 'L' and i+2 < size:
            if s[i:i+3] == 'LLL':
                return False

        elif s[i] == 'A':
            count += 1
            if count > 1:
                return False

    return True
