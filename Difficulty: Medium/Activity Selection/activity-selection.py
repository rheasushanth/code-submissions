class Solution:
    def activitySelection(self, start, finish):
        #code here
        act = list(zip(finish,start))
        act.sort()
        count = 1
        last = act[0][0]
        for (i,j) in act:
            if j>last:
                count+=1
                last = i
        return count