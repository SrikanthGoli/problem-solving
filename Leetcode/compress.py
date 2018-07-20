
# 443. String Compression

def compress(chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    i = 0
    count = 1
    output = []

    while i < len(chars)-1:
        if chars[i] == chars[i+1]:
            count += 1

        elif chars[i] != chars[i+1]:
            output.append(chars[i])
            for j in str(count):
                output.append(j)

            count = 1

        i += 1

    if count > 1:
        output.append(chars[i])
        for i in str(count):
            output.append(i)

    return output

input = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(compress(input))