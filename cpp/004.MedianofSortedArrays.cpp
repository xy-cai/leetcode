//转化为找第k小问题，然后将k分成两部分在两个数组中找，从而减小规模，递归实现

int findKth(vector<int>& a, int ab, int ae, vector <int>& b, int bb, int be, int k)
{
    if (ae-ab>be-bb) return findKth(b, bb, be, a, ab, ae, k); // b is longer than a
    if (ae == ab) return b[bb+k-1];
    if (k==1) return min(a[ab], b[bb]); // 边界情况
    int ak2_pos = min(ae-ab, k/2);
    int bk2_pos = k-ak2_pos;
    int ak2 = a[ab+ak2_pos-1];
    int bk2 = b[bb+bk2_pos-1];
    if (ak2<bk2)
        return findKth(a, ab+ak2_pos, ae, b, bb, be, k-ak2_pos); //注意下标，带上beginning
    else if (ak2>bk2)
        return findKth(a, ab, ae, b, bb+bk2_pos, be, k-bk2_pos);
    else
        return ak2;
}

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int len_1 = nums1.size();
        int len_2 = nums2.size();
        int tot = len_1 + len_2;
        if (tot&1)
            return findKth(nums1, 0, len_1, nums2, 0, len_2, tot/2+1);
        else
            return (findKth(nums1, 0, len_1, nums2, 0, len_2, tot/2)
                + findKth(nums1, 0, len_1, nums2, 0, len_2, tot/2+1))/2.0;
    }
};