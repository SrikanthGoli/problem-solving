class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums, self.idx = [], {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.idx:
            self.nums.append(val)
            self.idx[val] = len(self.nums) - 1
            return True

        return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.idx:
            pop, index = self.nums[-1], self.idx[val]
            self.nums[index], self.idx[pop] = pop, index
            self.nums.pop();
            del self.idx[val]
            return True

        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
