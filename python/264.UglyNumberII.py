class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ug = [1]
        a2 = 0 
        a3 = 0
        a5 = 0
        for i in range(1,n):
            tem = min(ug[a2]*2, min(ug[a3]*3, ug[a5]*5))
            ug.append(tem)
            if tem == ug[a2]*2: 
                a2+=1
            if tem == ug[a3]*3: 
                a3+=1
            if tem == ug[a5]*5: 
                a5+=1
        return ug[n-1]