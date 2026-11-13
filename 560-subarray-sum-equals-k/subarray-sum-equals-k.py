class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0:1}
        count  = 0
        total = 0
        for num in nums:
            total+= num

            target = total - k
            if target in prefix:
                count+=prefix[target]
            if total not in prefix:
                prefix[total] = 0
            prefix[total] += 1
        return count
        