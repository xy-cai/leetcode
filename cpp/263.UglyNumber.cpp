class Solution {
public:
    bool isUgly(int num) {
        if (num<1) return false;
        int prime[4] = {2,3,5,7};
        int ppos = 0;
        while(num!=1)
        {
            if (num%prime[ppos]) ppos++;
            else num/=prime[ppos];
            if (ppos==3) break;
        }
        if (ppos==3) return false;
        return true;
    }
};