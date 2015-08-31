class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 0:
            return 0

        mx = nums[0]
        i = 2
        while i<n:
            nums[i] = mx+nums[i]
            if mx < nums[i-1]:
                mx = nums[i-1]
            i+=1
        return max(nums)