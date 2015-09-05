class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        # hehe
        
        
        ret = 0
        minors = 0
        plus = 0
        proc = 1
        for ele in str:
            if ele in '0123456789':
                ret *= 10
                ret += int(ele)
                proc = 0
            elif ele == '-':
                minors += 1
                proc = 0
            elif ele == '+':
                plus += 1
                proc = 0
            elif ele == ' ' and proc:
                continue
            else:
                break
        if plus+minors>1:
            return 0
        if minors:
            ret *= -1
        if ret>2147483647:
            ret = 2147483647
        if ret < -2147483648:
            ret = -2147483648
        return ret