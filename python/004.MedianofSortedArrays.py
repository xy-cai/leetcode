def findKth(a, ab, ae, b, bb, be, k):
    if (ae-ab>be-bb):
        return findKth(b, bb, be, a, ab, ae, k)
    if (ae-ab==0):
        return b[bb+k-1]
    if (k==1):
        return min(a[ab],b[bb])
    
    ak2_pos = min(ae-ab, k/2)
    bk2_pos = k-ak2_pos
    ak2 = a[ab+ak2_pos-1]
    bk2 = b[bb+bk2_pos-1]
    if (ak2<bk2):
        return findKth(a, ab+ak2_pos, ae, b, bb, be, k-ak2_pos)
    elif (ak2>bk2):
        return findKth(a, ab, ae, b, bb+bk2_pos, be, k-bk2_pos)
    else:
        return ak2

class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        tot = len1+len2
        if tot%2 == 1:
            return findKth(nums1, 0, len1, nums2, 0, len2, tot/2+1)
        return (findKth(nums1, 0, len1, nums2, 0, len2, tot/2)+findKth(nums1, 0, len1, nums2, 0, len2, tot/2+1))/2.0
    