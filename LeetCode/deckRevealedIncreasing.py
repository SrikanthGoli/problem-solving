def deckRevealedIncreasing(deck):
    """
    :type deck: List[int]
    :rtype: List[int]
    """
    N = len(deck)
    index = collections.deque(range(N))
    res = [0] * N;
    deck.sort()

    for i in deck:
        res[index.popleft()] = i

        if index:
            index.append(index.popleft())

    return res