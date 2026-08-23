class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        time complexity : O(log n)
        space complexity : O(1)
        problem : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
        approach : 
        Keep track of two integers standing for two pointers l (left), r (right).
        If nums[0] <= nums[-1], this means either the length of array nums is 1 or the array itself is ascending, so just return nums[0].
        While l <= r, we calculate the mid point m (m = (l + r) // 2); if nums[m] < nums[m-1],
        this means we found the answer nums[m]; if nums[m] >= nums[0] (meaning m is on the left increasing part), 
        we will move l to m + 1 to search the right part; if nums[m] < nums[0], we will move r to m - 1 to search the left part.
        The reason we write "nums[m] >= nums[0]" instead of "nums[m] > nums[0]" is that if the length of array is 2 and nums[1] < nums[0], since (0 + 1) // 2 = 0, 
        we need to move l to m + 1 not r to m - 1.
        """
        if nums[0] <= nums[-1]:
            return nums[0]
        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < nums[m - 1]:
                return nums[m]
            if nums[m] >= nums[0]:
                l = m + 1
            else:
                r = m - 1
        return -1
