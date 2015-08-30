class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 1, 10, 100  <810
        
        def dfs(n, visit):
            #print n
            if visit[n] == 1:
                return False

            visit[n] = 1

            if n == 1:
                return True
                
            tem = 0
            while n:
                tem += (n%10)**2
                n /= 10
            return dfs(tem, visit)
        
        visit = [0]*900
        tem = 0
        while n:
            tem += (n%10)**2
            n /= 10
            
        return dfs(tem, visit)
