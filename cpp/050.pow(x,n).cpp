class Solution {
public:
    double myPow(double x, int n) {
        long long lln = n;
        double neg = false;
        if (lln<0) 
        {
            neg = true;
            lln = -lln;
        }
        
        double p[33];
        p[0] = x;
        for (int i=1;i<33;++i)
        {
            p[i] = p[i-1]*p[i-1];
        }
        bool bits_n[33];
        for (int i=0;i<33;++i) bits_n[i] = false;
        int bpos = 0;
        long long tem_n = lln;
        while(tem_n)
        {
            bits_n[bpos++] = (tem_n & 1);
            tem_n = (tem_n >> 1);
        }
        double ret = 1;
        for (int i=0;i<33;++i)
        {
            if (bits_n[i])
            {
                ret *= p[i];
            }
        }
        if (neg) ret = 1/ret;
        return ret;
    }
};