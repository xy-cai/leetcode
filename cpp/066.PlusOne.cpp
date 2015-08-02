class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int len = digits.size();
        vector <int> ret;
        int flag = 0;
        digits[len-1]++;
        for (int i=len-1;i>=0;--i)
        {
            int tem = digits[i]+flag;
            flag = tem / 10;
            digits[i] = tem % 10;
        }
        ret.clear();
        if (flag)
        {
            ret.push_back(1);
        }
        ret.insert(ret.end(), digits.begin(), digits.end());
        return ret;
    }
};