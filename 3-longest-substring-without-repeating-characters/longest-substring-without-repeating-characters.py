class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        best = 0
        st = set()
        for right in range(len(s)):
            while s[right] in st: 
                st.remove(s[left])
                left += 1
            st.add(s[right])
            best = max(best, right - left + 1)
        return best





        