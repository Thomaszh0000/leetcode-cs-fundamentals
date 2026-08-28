# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        n = number of nodes
        h = height of the tree
        time complexity : O(n)
        space complexity : O(h) since we are using recursion
        problem : https://leetcode.com/problems/validate-binary-search-tree/
        approach : 
        Define a function dfs(node, minB, maxB) which minB and maxB stand for left and right boundary separately.
        In the function : if node does not exists, return True; if node.val >= maxB or node.val <= minB, return False; 
        if we pass all the tests, 
        we are sure that node.val is inside (minB, maxB) so we will then return dfs(node.left, minB, node.val) and dfs(node.right, node.val, maxB). 
        (Use node.val as new boundary since we are sure that its value is inside (minB, maxB))
        Finally, return the answer dfs(root, float('-inf'), float('inf')).
        """
        def dfs(node, minB, maxB):
            if not node:
                return True
            if node.val >= maxB or node.val <= minB:
                return False
            return dfs(node.left, minB, node.val) and dfs(node.right, node.val, maxB)
        return dfs(root, float('-inf'), float('inf'))
