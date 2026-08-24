# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        time complexity : O(n)
        space complexity : O(1)
        problem : https://leetcode.com/problems/reverse-linked-list/
        approach :
        If head does not exist, we will just return None.
        If head exists, we will keep track of two pointer: prev and cur, which are initialized to None and head seperately.
        Then we use a while-loop for reversation : while cur exist, we use temp to store cur.next, then set cur.next to prev, we then set prev to cur and cur to temp.
        Finally, we'll return our answer prev(since cur will be None at this time and cur will be the last one).
        """
        if not head:
            return None
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
