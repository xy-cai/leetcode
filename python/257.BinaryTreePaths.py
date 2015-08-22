# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def dfs(root, path, ret):
    path.append(root.val)
    if root.left == None and root.right == None:
        s = '->'.join(str(i) for i in path)  #great python!
        ret.append(s)
        
    if root.left:
        dfs(root.left, path, ret)
    if root.right:
        dfs(root.right, path, ret)
    path.pop()
    

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root == None:
            return []
        ret = []
        path = []
        dfs(root, path, ret)
        return ret