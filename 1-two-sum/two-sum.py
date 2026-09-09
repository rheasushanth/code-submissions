class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i,n in enumerate(nums):
            comp = target - n
            if comp in seen:
                return [seen[comp],i]
            seen[n] = i
        return []

        