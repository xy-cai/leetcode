class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        nums_len = len(nums)
        for ele in nums:
        	sum += ele
        return nums_len*(nums_len+1)/2-sum