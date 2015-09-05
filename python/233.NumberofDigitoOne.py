class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        # calculate for every digit position
        cnt = 0
        w = 1
        while w <= n:
            a = n/(10*w)
            b = n%(10*w)
            cnt += a*w
            if b>=w and b<2*w:
                cnt += b-w+1
            elif b>=2*w:
                cnt += w
            w *= 10
        return cnt

s = Solution()
print s.countDigitOne(20)