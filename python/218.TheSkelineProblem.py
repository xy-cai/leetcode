class IntvalTree:
    def __init__(self):
        self.left = None
        self.right = None
        self.mx = 0
        self.cnt = 0
        self.flag = False

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        # 线段树+离散化
        
        if not len(buildings):
            return []

        lines = []
        mxh = -1
        heights = []
        for ele in buildings:
            if mxh<ele[2]:
                mxh = ele[2]
            heights.append(ele[2])
            lines.append((ele[0], ele[1], ele[2], 1))
            lines.append((ele[1], ele[0], ele[2], -1))
        lines = sorted(lines, key=lambda x:x[0])
        # print lines

        heights.sort()
        lenh = len(heights)

        tree = []
        for i in range(0,4*lenh+5):
            tree.append(IntvalTree())

        def build_tree(id, l, r):
            # print (id<<1)+1, (id+1)<<1
            tree[id].left = l
            tree[id].right = r
            tree[id].flag = False
            if l == r:
                tree[id].flag = True
                tree[id].cnt = 0
                return
            mid = (l+r)>>1
            build_tree((id<<1)+1, l, mid)
            build_tree((id+1)<<1, mid+1, r)

        def add_tree(id, val):
            if (tree[id].mx<val):
                tree[id].mx = val
            if tree[id].flag:
                tree[id].cnt += 1
                return
            mid = heights[tree[(id<<1)+1].right]
            if val>mid:
                add_tree((id+1)<<1, val)
            else:
                add_tree((id<<1)+1, val)

        def del_tree(id, val):
            if tree[id].flag:
                tree[id].cnt -= 1
                if not tree[id].cnt:
                    tree[id].mx = 0
                return
            mid = heights[tree[(id<<1)+1].right]
            if val>mid:
                del_tree((id+1)<<1, val)
            else:
                del_tree((id<<1)+1, val)

            tree[id].mx = max(tree[(id<<1)+1].mx, tree[(id+1)<<1].mx)

        cur = -1
        build_tree(0, 0, lenh-1)
        kpts = []
        for ele in lines:
            if ele[3] == 1:
                add_tree(0, ele[2])
            else:
                del_tree(0, ele[2])

            while len(kpts) and kpts[-1][0] == ele[0]:
                kpts.pop()
                if len(kpts):
                    cur = kpts[-1][1]
                else:
                    cur = -1

            # print ele, kpts
            # print ele[3], ele[2], tree[0].mx
            if cur != tree[0].mx:
                cur = tree[0].mx
                kpts.append([ele[0], cur])

            # print kpts
        
        return kpts