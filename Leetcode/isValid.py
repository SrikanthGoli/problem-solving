# 20. Valid Parentheses

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

    helper_dict = {")": "(", "}": "{", "]": "["}
    stack = []
    size = len(s)

    if size == 0:
        return True

    if size > 1 and size % 2 == 0:

        for i in range(len(s)):
            if s[i] in "[{(":
                stack.append(s[i])
            elif len(stack) > 0:
                key = stack.pop()
                if helper_dict[s[i]] != key:
                    return False

        if len(stack) == 0:
            return True

    return False