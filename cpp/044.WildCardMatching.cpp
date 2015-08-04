class Solution {
public:
    bool isMatch(string s, string p) {
        
        int len_s = s.length();
        int len_p = p.length();
        string pp = "";
        if (len_p)
        {
            pp = p[0];
            for (int i=1;i<len_p;++i)
            {
                if (!(p[i] == '*' && p[i] == p[i-1]))
                    pp += p[i];
            }
            len_p = pp.length();
        }
        
        bool **dp = new bool* [len_s+1];
        bool **dprow = new bool* [2];
        dprow[0] = new bool [len_s+1];
        dprow[1] = new bool [len_s+1];
        for (int i=0;i<=len_s;++i)
        {
            dp[i] = new bool[len_p+1];
        }
        
        dp[0][0] = true;
        
        for (int i=1;i<=len_s;++i)
            dp[i][0] = false;
        
        for (int i=0;i<=len_s;++i)
            dprow[0][i] = true;
            
        int f = 1;
        
        for (int j=1;j<=len_p;++j)
        {
            for (int i=0;i<=len_s;++i)
            {
                dp[i][j] = false;
                
                if (pp[j-1] == '*')
                {
                    if (dprow[1-f][i]) dp[i][j] = true;
                }
                else if (pp[j-1] == '?')
                {
                    if (i && dp[i-1][j-1]) dp[i][j] = true;
                }
                else 
                {
                    if (i && pp[j-1] == s[i-1] && dp[i-1][j-1]) dp[i][j] = true; 
                }
                
                if (dp[i][j]) {dprow[f][i] = true;continue;}
                if (i && dprow[f][i-1]) {dprow[f][i] = true;continue;}
                dprow[f][i] = false;
                
            }
            
            f = 1-f;
        }
        
        
        return dp[len_s][len_p];
    }
};