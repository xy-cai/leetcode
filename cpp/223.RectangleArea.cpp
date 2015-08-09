class Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int area = (C-A)*(D-B)+(G-E)*(H-F);
        int x = max(A,E);
        int y = max(B,F);
        int a = min(C,G);
        int b = min(D,H);
        if (x>a || y>b) return area;
        return area-(a-x)*(b-y);
    }
};