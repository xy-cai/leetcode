class Solution {
public:
    string minWindow(string s, string t) {
        int len_s = s.length();
        int len_t = t.length();
        int rest = 0;  // 字符种类个数
        int visit[256];
        for (int i=0;i<256;++i) visit[i] = -1e9;
        for (int i=0;i<len_t;++i) 
        {
            if(visit[t[i]]==-1e9) 
            {
                visit[t[i]] = 0;
                rest++;
            }
            visit[t[i]]++;
        }
        int p=0,q=-1;
        bool expand = true;
        
        int res_p, res_q, res = len_s+1;
        while (p<len_s && q<len_s)
        {
            if (expand)
            {
                ++q;
                if (visit[s[q]]==-1e9) continue;
                visit[s[q]]--; //可以出现负的，表明多余的字符
                if (!visit[s[q]])
                    rest--;
                if (!rest)
                    expand = false;
            }
            else
            {
                if (visit[s[p]]==0)
                {
                    if (res > q-p+1)
                    {
                        res = q-p+1;
                        res_q = q;
                        res_p = p;
                    }
                    visit[s[p]]++;
                    rest++;
                    p++;
                    expand = true;
                }
                else if (visit[s[p]]!=-1e9)
                {
                    visit[s[p]]++;
                    p++;
                }
                else p++;
            }
        }
        if (res == len_s+1) return "";
        return s.substr(res_p, res_q-res_p+1);
    }
};