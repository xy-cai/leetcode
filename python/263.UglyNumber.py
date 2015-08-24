class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        if num<1:
            return False  #:(
        prime = [2,3,5,7]
        ppos = 0
        while num != 1:
            if num%prime[ppos]:
                ppos += 1
            else:
                num /= prime[ppos]
            if prime[ppos] == 7:
                break
        if prime[ppos]==7:
            return False
        return True
