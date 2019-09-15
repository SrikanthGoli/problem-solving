def threeSumSmaller(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    nums.sort()
    N, res = len(nums), 0

    for i, x in enumerate(nums):

        s = target - x
        j, k = i + 1, N - 1

        while j < k:
            if nums[j] + nums[k] < s:
                res += k - j
                j += 1
            else:
                k -= 1

    return res