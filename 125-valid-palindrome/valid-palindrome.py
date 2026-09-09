class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sp = [c.lower() for c in s if c.isalnum()]
        l = 0
        r = len(sp) - 1
        while l<r:
            if sp[l] != sp[r]:
                return False
            l+=1
            r-=1
        return True


        