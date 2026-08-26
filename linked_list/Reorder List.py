# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        n = number of ListNode
        time complexity : O(n)
        space complexity : O(1)
        problem : https://leetcode.com/problems/reorder-list/
        approach : 
        We first keep track of two pointers fast and slow pointed at head. 
        While fast.next and fast.next.next exist, 
        we will set fast to fast.next.next and slow to slow.next, 
        therefore slow will go to the (n//2 + 1)th (if n is odd) or (n//2)th (if n is even) ListNode, 
        we will then set second to slow.next, prev to None and slow.next to None (we want to split the whole list into two halves).
        Then use while-loop : while second exists, we will set ns to second.next, second.next to prev, prev to second, 
        second to ns (so we can reverse the direction how every ListNode points at each other in the second sublist).
        We will then set first to head, second to prev.
        Use a while loop : while second exists, set n1 to first.next, n2 to second.next.
        Then we set first.next to second, second.next to n1. After that, set first to n1, second to n2.
        Complete.
        """
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        prev = None
        slow.next = None
        while second:
            ns = second.next
            second.next = prev
            prev = second
            second = ns
        first, second = head, prev
        while second:
            n1, n2 = first.next, second.next
            first.next = second
            second.next = n1
            first = n1
            second = n2
