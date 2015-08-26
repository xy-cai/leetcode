import math
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ret = [0]*n
        ret[-1] = 1
        left = 1
        for i in range(n-2,-1,-1):
            ret[i] = ret[i+1]*nums[i+1]
        for i in range(0,n-1):
            ret[i] = left*ret[i]
            left *= nums[i]
        ret[-1] = left
        return ret
