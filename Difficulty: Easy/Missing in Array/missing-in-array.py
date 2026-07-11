class Solution:
    def missingNum(self, arr):
        n = len(arr) + 1
        asum = sum(arr)
        tsum = n * (n+1) // 2
        return tsum - asum
        
        
            
        