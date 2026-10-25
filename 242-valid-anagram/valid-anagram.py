class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        if len(s) != len(t):
            return False
        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        for chs in t:
            if chs in freq:
                freq[chs]-=1
        for k in freq:
            if freq[k] != 0:
                return False
        return True

            
        