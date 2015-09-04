class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # delete two different num
        # then the majority element will be the rest
        
        # candidate = nums[0]
        cnt = 0
        for ele in nums:
            if cnt:
                if candidate == ele:
                    cnt += 1
                else:
                    cnt -= 1
                
            else:
                candidate = ele
                cnt = 1
                
        return candidate