#include <vector>

class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows==1) return s;
        vector <string> sub(numRows, "");
        string ret = "";
        int len = s.length();
        bool dir = true;
        int idx = 0;
        for (int i=0;i<len;++i)
        {
            sub[idx] += s[i];
            if (idx==numRows-1) dir = false;
            else if (idx==0) dir = true;
            if (dir) idx++;
            else idx--;
        }
        for (int i=0;i<numRows;++i)
            ret += sub[i];
        return ret;
    }
};