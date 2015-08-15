class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x<0:
            return False
        ori = x
        tem = 0
        while x:
            tem *= 10
            tem += x%10
            x /= 10
        if tem == ori:
            return True
        return False