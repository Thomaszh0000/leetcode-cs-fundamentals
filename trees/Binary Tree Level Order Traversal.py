from __future__ import annotations

from typing import List, Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        n = number of nodes
        m = widest level's number of nodes
        space complexity : O(m)
        time complexity : O(n)
        problem : https://leetcode.com/problems/binary-tree-level-order-traversal/
        approach :
        If root does not exists, we will just return [].
        If root does exists, we will declare an array res and set it to []. 
        We then create an array "current" initialized to [root] storing current processing items.
        Use while-loop : while current -> append [] to res and declare an array temp (storing the next current array) initialized to []. 
        Use a for-loop, for cur in current, append cur.val to res[-1], then append cur.left and cur.right to temp if they exist separately.
        Finally, we will return res.
        """
        if not root:
            return []
        res = []
        current = [root]
        while current:
            res.append([])
            temp = []
            for cur in current:
                res[-1].append(cur.val)
                if cur.left:
                    temp.append(cur.left)
                if cur.right:
                    temp.append(cur.right)
            current = temp
        return res
