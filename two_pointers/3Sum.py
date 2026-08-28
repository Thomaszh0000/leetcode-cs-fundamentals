class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        n = length of nums
        time complexity : O(n^2)
        space complexity : O(1)
        problem : https://leetcode.com/problems/3sum/
        approach :
        Create an array "res" and sort nums in increasing order.
        Use for-loop -> for i in [0, n-3], if i > 0 and nums[i] equals nums[i-1], we will skip this iteration (means we met a same number); 
        we then set target to - nums[i] and set pointer left to i + 1, right to n - 1; 
        use while loop -> while left < right, if nums[left] + nums[right] equals target, append [nums[i], nums[left], nums[right]] to res, 
        and while left < right and nums[left] equals nums[left + 1], increment left (means we met a same number), 
        while left < right and nums[right] equals nums[right - 1], decrement right (means we met a same number); 
        we then increment left and decrement right again. If nums[left] + nums[right] < target, we increment left; otherwise, we decrement right.
        After the outer for-loop, we return the answer res.
        """
        res = []
        n = len(nums)
        nums.sort()
        for i in range(0, n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = - nums[i]
            left, right = i + 1, n - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                    left += 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return res
