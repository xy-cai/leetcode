class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        dir = True
        idx = 0
        len_s = len(s)
        sub = [];
        for i in range(0,numRows):
            sub.append("")
        for i in range(0,len_s):
            sub[idx] += s[i]
            if (idx==numRows-1):
                dir = False
            elif (idx==0):
                dir = True
            if dir:
                idx += 1
            else:
                idx -= 1
        ret = ""
        for i in range(0,numRows):
            ret += sub[i]
        return ret
        