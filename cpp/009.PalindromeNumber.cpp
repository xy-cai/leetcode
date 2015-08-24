class Solution {
public:
    bool isPalindrome(int x) {
        //if (x==0) return true;
        //x = abs(x);
        if (x<0) return false;
        int tem = 0;
        int ori = x;
        while(x)
        {
            tem *= 10;
            tem += x%10;
            x /= 10;
        }
        if (tem==ori) return true;
        return false;
    }
};