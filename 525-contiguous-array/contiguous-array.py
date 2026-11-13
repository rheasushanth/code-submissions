class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        '''
        best = length = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                sub = nums[i:j]
                zeros = ones = 0
                for k in range(len(sub)):
                    if sub[k] == 0:
                        zeros+=1
                    if sub[k] == 1:
                        ones +=1
                if zeros == ones:
                    length = len(sub)
            best = max(best, length)
        return best
        '''

        first = {0:-1}
        count = 0
        best = 0
        for i in range(len(nums)):
            count+=1 if nums[i] == 1 else -1
            if count in first:
                best = max(best, i - first[count])
            else:
                first[count] = i
        return best

        