class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nor = 0
        for ele in nums:
            nor ^= ele
        sht = 0
        while not (nor>>sht)&1:
            sht += 1
        nor2 = 0
        for ele in nums:
            if (ele>>sht)&1:
                nor2 ^= ele
        ret = [nor2, nor^nor2]
        return ret