def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    n = len(nums);
    res = set()
    nums.sort()

    for i in range(n):
        key = 0 - nums[i]
        j, k = i + 1, n - 1

        while j < k:
            s = nums[j] + nums[k]
            if s == key:
                res.add((nums[i], nums[j], nums[k]))
                j += 1
                k -= 1
            elif s > key:
                k -= 1
            else:
                j += 1

    return list(res)