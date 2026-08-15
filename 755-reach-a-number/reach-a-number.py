class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        sumn = 0
        n = 0
    
        while sumn < target:
            n+=1
            sumn+=n
        while (sumn - target) % 2 != 0:
                n+=1
                sumn += n
        return n

        


        