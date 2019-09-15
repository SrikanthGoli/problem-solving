class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = [];
        nums.append(float('inf'))
        i, j = 0, 0

        while j < len(nums) - 1:
            i = j

            while j < len(nums) and nums[j + 1] == nums[j] + 1:
                j += 1

            if i == j:
                res.append(str(nums[i]))
            else:
                res.append(str(nums[i]) + '->' + str(nums[j]))

            j += 1

        return res

    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res, start, end = [], -1, -1

        nums = [float('inf')] + nums
        nums.append(float('inf'))

        for i in range(1, len(nums) - 1):

            if nums[i] - 1 != nums[i - 1]:
                start = nums[i]
            if nums[i] + 1 != nums[i + 1]:
                end = nums[i]
                if start == end:
                    res.append(str(start))
                else:
                    res.append(str(start) + '->' + str(end))

        return res