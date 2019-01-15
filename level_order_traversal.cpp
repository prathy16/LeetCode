# https://leetcode.com/problems/binary-tree-level-order-traversal/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> levelOrder;
        if(!root){
            return levelOrder;
        }
        
        queue<TreeNode*> temp;
        queue<TreeNode*> nodes;
        vector<int> level;
        
        temp.push(root);
        
        while(!temp.empty())
        {
            TreeNode* t = temp.front();
            temp.pop();
            
            level.push_back(t->val);
            
            if(t->left)  nodes.push(t->left);
            if(t->right) nodes.push(t->right);
            
            if(temp.empty())
            {
                temp.swap(nodes);
                levelOrder.push_back(level);
                level.clear();
            }
        }
        
        return levelOrder;
    }
};
