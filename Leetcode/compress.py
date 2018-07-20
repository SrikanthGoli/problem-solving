
# 443. String Compression

def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    i = 0
    count = 1
    helper_str = ""

    if len(chars) == 1:
        return len(chars)

    while i < len(chars)-1:
        if chars[i] == chars[i+1]:
            count += 1

        elif chars[i] != chars[i+1]:
            helper_str += chars[i]
            if count > 1:
                helper_str += str(count)

            count = 1
        i += 1

    helper_str += chars[i]
    if count > 1:
         helper_str += str(count)

    chars[:len(helper_str)] = helper_str

    return (chars[:len(helper_str)])