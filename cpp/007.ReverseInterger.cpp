//关键题目里也没说爆int返回0啊。。

class Solution {
public:
    int reverse(int x) {
        bool flag = (x<0);
        int b[32];
        int blen=0;
        long long tem = abs(x);
        while(tem)
        {
            b[blen++] = tem%10;
            tem /= 10;
        }
        tem = 0;
        for (int i=0;i<blen;++i)
        {
            tem *= 10;
            tem += b[i];
        }
        if (flag) tem *= -1;
        if (tem>((1LL<<31)-1)) tem = 0;
        if (tem<(-1LL<<31)) tem = 0;
        return tem;
    }
};