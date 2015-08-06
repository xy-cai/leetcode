class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector <int> ret;
        ret.clear();
        int len = nums.size();
        if (len==0) return ret;
        
        vector <int> mx;
        mx.clear();
        mx.push_back(0);
        for (int i=1;i<len-1;++i)
            if (nums[i]>nums[i-1] && nums[i]>nums[i+1]) mx.push_back(i);
        if (nums[len-1]>nums[len-2]) mx.push_back(len-1);
        int mx_len = mx.size();
        int cur = nums[0];
        int mx_pos = -1;
        int dom_pos = 0;
        int dom_mx_pos = -1;
        for (int i=k-1;i<len;++i)
        {
            if (dom_pos<i-k+1)
            {
                dom_pos++;
                cur = nums[dom_pos];
                mx_pos = dom_mx_pos;
                while(mx_pos+1<mx_len && mx[mx_pos+1]<=dom_pos) mx_pos++;
            }
            while(mx_pos+1<mx_len && mx[mx_pos+1]<=i)
            {
                mx_pos++;
                if (cur<nums[mx[mx_pos]])
                {
                    cur = nums[mx[mx_pos]];
                    dom_pos = mx[mx_pos];
                    dom_mx_pos = mx_pos;
                }
            }
            if (cur<nums[i])
            {
                dom_pos = i;
                cur = nums[i];
            }
            ret.push_back(cur);
        }
        return ret;
    }
};