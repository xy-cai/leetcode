class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int nor = 0;
        int len = nums.size();
        for (int i=0;i<len;++i)
        {
            nor ^= nums[i];
        }
        int sht = 0;
        while (!((nor>>sht)&1)) sht++;  // find the last 1 of nor
        int nor2 = 0;
        for (int i=0;i<len;++i)
        {
            if ((nums[i]>>sht)&1) nor2 ^= nums[i];
        }
        vector <int> ret;
        ret.push_back(nor2);
        ret.push_back(nor^nor2);
        return ret;
    }
};