class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        i = 0

        for i in range(len(s)):
            if s[i]== '{' or s[i ]== '[' or s[i] == '(':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                a = stack.pop()
                if s[i] == '}' and a != '{':
                    return False 
                elif s[i] == ']' and a != '[':
                    return False 
                elif s[i] == ')' and a != '(':
                    return False 
        return len(stack) == 0