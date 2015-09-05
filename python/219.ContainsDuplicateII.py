class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
        d = {}
        for i in range(0, n):
            if i-k-1>=0:
                d.pop(nums[i-k-1])
            if nums[i] in d:
                return True
            else:
                d[nums[i]] = i
        return False