# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        time complexity : O(n)
        space complexity : O(1), excluding the output list.
        problem : https://leetcode.com/problems/add-two-numbers/
        approach : 
        Create a ListNode object dummy, and keep track of an integer carry (initialized to 0) and pointer cur (pointed to dummy at first). 
        Use a while-loop to operate iteration, while l1 exists or l2 exists or carry not eqauls to 0, we set v1 to l1.val if l1 exist else set it to 0, 
        v2 to l2.val if l2 exist else set it to 0, set cur.next to a new ListNode, 
        and set its value to (v1 + v2 + carry) % 10, then set cur to cur.next and carry to (v1 + v2 + carry) // 10. 
        Finally, we set l1 to l1.next if l1 exist else set it to None, do the same thing to l2. 
        Therefore if l1 and l2 eqauls to None and carry eqauls to 0, the while-loop will be breaked. We will then return our answer dummy.next.
        The reason we use a dummy ListNode is that if we create a new ListNode after we set value to current ListNode in while loop, 
        this will leave a ListNode whose value is 0 in the end.
        """
        dummy = ListNode()
        carry = 0
        cur = dummy
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            cur.next = ListNode((v1 + v2 + carry) % 10)
            cur = cur.next
            carry = (v1 + v2 + carry) // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
