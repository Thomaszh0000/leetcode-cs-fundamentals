class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        space complexity : O(1)
        time complexity : O(log n)
        problem:
        https://leetcode.com/problems/binary-search/
        approach:
        Keep track of two pointers, l (left) and r (right). 
        While the l is less than or equal to r (using a while loop), calculate the midpoint index m. 
        If nums[m] equals to target, we have found the answer and return m.
        If nums[m] is not equal to target, we will move r to m - 1 if target is smaller than nums[m] (search the left part), 
        move l to m + 1 if target is bigger than nums[m] (search the right part).
        If l > r, it will break the while loop, this means the target isn't in the input array.
        """
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m-1
            else:
                l = m+1
        return -1
