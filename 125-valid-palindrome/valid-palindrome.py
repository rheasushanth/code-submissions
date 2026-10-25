class Solution:
    def isPalindrome(self, s: str) -> bool:
        sc = [ch.lower() for ch in s if ch.isalnum()]
        if sc == sc[::-1]:
            return True
        return False
