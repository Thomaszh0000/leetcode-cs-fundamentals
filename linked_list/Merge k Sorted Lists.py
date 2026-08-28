from __future__ import annotations

from typing import List, Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        k = number of linked lists (the one that the problem gave)
        n = number of ListNodes
        time complexity : O(n * log k)
        space complexity : O(k)
        problem : https://leetcode.com/problems/merge-k-sorted-lists/
        approach :
        We first declare an array "heap", for i, node in enumerate(lists), 
        if node exists, we will then use heappush to push (node.val, i, node) to heap
        (the reason we use i is that node object can't be compared but integer i can).
        We then instantiate a ListNode object dummy, and points pointer "cur" to dummy.
        Use a while-loop : while heap is not empty list, 
        we will use heappop to retrieve the smallest node, its value and index (the one created when we created heap using enumeration). 
        We will then set cur.next to node;
        if node.next exists, we will set then use heappush to push the next node's value, index (will therefore be the same one), 
        node object to heap; after that, set cur to cur.next.
        Finally, return our answer dummy.next.
        """
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        dummy = ListNode()
        cur = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = node
            if node.next:
                node = node.next
                heapq.heappush(heap, (node.val, i, node))
            cur = cur.next
        return dummy.next
