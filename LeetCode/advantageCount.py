def advantageCount(A, B):
    """
    :type A: List[int]
    :type B: List[int]
    :rtype: List[int]
    """
    A = sorted(A)
    dic = collections.defaultdict(list)

    for b in sorted(B)[::-1]:
        if b < A[-1]:
            dic[b].append(A.pop())

    return [(dic[b] or A).pop() for b in B]
