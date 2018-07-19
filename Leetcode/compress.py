
# 443. String Compression

def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    helper_dict = {}
    count = 0
    for i in chars:
        if i in helper_dict:
            helper_dict[i] += 1
        else:
            helper_dict[i] = 1

    for i in sorted(set(chars)):
        if helper_dict[i] > 1:
            chars[count] = i
            count += 1
            chars[count] = (str(helper_dict[i]))
            count += 1
        else:
            chars[count] = i
            count += 1

    return chars[:count]

input = ["a","a","b","b","c","c","c"]
print(compress(input))