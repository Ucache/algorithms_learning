/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> ret;
    vector<int> inorderTraversal(TreeNode *root) {
        vector<int> ret;
        if(!root) return ret;
        stack<TreeNode*> Q;
        while(Q.size()||root)
        {
            while(root)
            {
                Q.push(root);
                root=root->left;
                
            }
            TreeNode* front = Q.top();
            ret.push_back(front->val);
            Q.pop();
            root = front->right;
        }
        return ret;
    }
};