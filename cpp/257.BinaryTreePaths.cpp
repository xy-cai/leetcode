/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

#include <vector>
#include <string>

void dfs(TreeNode* node, vector <int> &path, vector <string> &ret)
{
    path.push_back(node->val);
    if (node->left == NULL && node->right == NULL) 
    {
        char str[10];
        sprintf(str, "%d", path[0]);
        string sstr = str;
        string s = sstr;
        for (int i=1;i<path.size();++i)
        {
            sprintf(str, "->%d", path[i]);
            sstr = str;
            s += sstr;
        }
        ret.push_back(s);
    }
    if (node->left) dfs(node->left, path, ret);
    if (node->right) dfs(node->right, path, ret);
    path.pop_back();
}

class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        vector <int> path;
        vector <string> ret;
        if (root==NULL) return ret;
        dfs(root, path, ret);
        return ret;
    }
};