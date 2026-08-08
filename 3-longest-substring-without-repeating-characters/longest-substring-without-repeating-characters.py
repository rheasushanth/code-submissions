class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        best = 0
        st = ""
        for right in range(len(s)):
            st+=s[right]
            while len(st) != len(set(st)):
                st = st.replace(s[left],"",1)
                left += 1
            best = max(best, right - left + 1)
        return best





        