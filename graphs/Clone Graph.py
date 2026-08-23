"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        n = number of edges
        m = number of nodes
        time complexity : O(n + m)
        space complexity : O(m)
        problem : https://leetcode.com/problems/clone-graph/
        approach : 
        If node is None, we will just return None.
        If node exists, we define a dict "seen" stores the mapping relationship between cloned nodes and real ones (for example, seen[real] = clone means "real" corresponds to "clone").
        We will first create a Node-class object "res" and set its value to the given node's value.
        Then define a function dfs(real, clone) which will iterate through all neighbor in real.neighbors, if neighbor does not exist in seen, we will create a Node-class object "temp" and set its value to neighbor's value, then append it to the clone's neighbors list, and then run dfs(neighbor, temp) to continue the deep-first-search; if the neighbor already exists in seen, we will just appends seen[neighbor] to clone.neighbors (since we don't want to have two object representing the same node and this can prevent infinite loop).
        Finally, execute dfs(node, res) and return the result res.
        """
        if not node:
            return None
        seen = {}
        res = Node(node.val)
        seen[node] = res
        def dfs(real, clone):
            for neighbor in real.neighbors:
                if neighbor not in seen:
                    temp = Node(neighbor.val)
                    seen[neighbor] = temp
                    clone.neighbors.append(temp)
                    dfs(neighbor, temp)
                else:
                    clone.neighbors.append(seen[neighbor])
        dfs(node, res)
        return res
