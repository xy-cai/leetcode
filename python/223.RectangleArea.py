class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        x = max(A,E)
        y = max(B,F)
        a = min(C,G)
        b = min(D,H)
        area1 = (C-A)*(D-B)
        area2 = (G-E)*(H-F)
        if a-x<0 or b-y<0:
            return area1+area2
        return area1+area2-(a-x)*(b-y)