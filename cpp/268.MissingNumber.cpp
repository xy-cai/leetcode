class Solution {
public:
    int missingNumber(vector<int>& nums) {
    	int len = nums.size();
    	int sum = 0;
    	for (int i=0;i<len;++i) sum += nums[i];
    	return (len*(len+1)>>1) - sum;
    }
};