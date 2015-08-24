class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        ret = 0
        while n:
            if n&1:
                ret += 1
            n >>= 1
        return ret
