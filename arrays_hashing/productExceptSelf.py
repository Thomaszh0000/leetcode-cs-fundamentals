class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        time complexity : O(n)
        space complexity : O(1)
        problem : 
        https://leetcode.com/problems/product-of-array-except-self/
        approach:
        We create an array "prefix". For each number in the array "num", we calculate its prefix (product of previous elements), 
        the first prefix will be 1. 
        Then, we keep track of a "suffix" integer (product of subsequent elements) and go backward to calculate suffix (for the last one, 
        it will be 1) for each element and use stored prefix values to generate answers.
        """
        n = len(nums)
        prefix = [0] * n
        prefix[0] = 1
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
        suffix = 1
        for i in range(n-1, -1, -1):
            prefix[i] *= suffix
            suffix *= nums[i]
        return prefix
