class Solution {
public:
    int nthUglyNumber(int n) {
        int *ug = new int[n];
        ug[0] = 1;
        int a2 = 0, a3 = 0, a5 = 0;
        for (int i=1;i<n;++i)
        {
            ug[i] = min(ug[a2]*2, min(ug[a3]*3, ug[a5]*5));
            // if ug[a2]*2 == ug[a3]*3, both ++
            if (ug[i] == ug[a2]*2) a2++;
            if (ug[i] == ug[a3]*3) a3++;
            if (ug[i] == ug[a5]*5) a5++;
        }
        return ug[n-1];
    }
};