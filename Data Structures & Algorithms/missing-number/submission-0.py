class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actual = sum(nums)
        exp = n*(n+1) // 2
        return exp - actual

        