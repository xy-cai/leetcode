class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        flag = (x<0)
        if flag:
            x = -x
        ret = 0
        while x:
            ret *= 10
            ret += x%10
            x /= 10
        if flag:
            ret = -ret
        if ret>(2**31-1) or ret<(-2**31):
            ret = 0
        return ret