class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        n = len(nums)
        d = {}
        for i in range(0, n):
            if i-k-1>=0:
                d.pop(nums[i-k-1])
            for kk in range(nums[i]-t, nums[i]+t+1):
                if kk in d:
                    return True
            d[nums[i]] = i
        return False

s = Solution()
print s.containsNearbyAlmostDuplicate([0,2147483647], 1, 2147483647)