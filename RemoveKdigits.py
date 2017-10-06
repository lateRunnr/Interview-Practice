class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        ## Base Case
        if len(num) == 1 and k == 1:
            return "0"
        if len(num) == 1 and k == 0:
            return num
        if len(num) == k:
            return "0"
        
        temp=[]
        for ch in num:
            while k and len(temp) > 0 and temp[-1] > ch:
                temp.pop()
                k-=1
            if not(len(temp) == 0 and ch == "0"):
                temp.append(ch)
                
        while k != 0:
            temp.pop()
            k-=1
        
        if temp:
            res=''.join(temp)
            return res
        else:
            return "0"
