class Solution {
public:
    bool isAnagram(string s, string t) {
        int cnt[256];
        for (int i=0;i<256;++i) cnt[i] = 0;
        int len_s = s.length();
        int len_t = t.length();
        if (len_s!=len_t) return false;
        for (int i=0;i<len_s;++i)
            cnt[s[i]]++;
        for (int i=0;i<len_t;++i)
            cnt[t[i]]--;
        for (int i=0;i<256;++i)
            if (cnt[i]) return false;
        return true;
    }
};