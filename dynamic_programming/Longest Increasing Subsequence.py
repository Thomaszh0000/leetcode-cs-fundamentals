import bisect
class Solution:
    """
    time complexity : O(n log n)
    space complexity : O(n)
    problem : https://leetcode.com/problems/longest-increasing-subsequence/
    approach : 
    Keep track of an array res. For each number in array nums, 
    if the number is bigger than res[-1], append it to the back; otherwise, 
    use binary search to find the position "pos" it should be located and change res[pos] to number. Finally, return the length of res.
    We use bisect.bisect_left because we want to make sure that the array will always keep track of the best result (for every element, as small as possible). The length of array will be changed only if there is a input number that is bigger than res[-1], this means we have found a longer increasing subsequence.
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [nums[0]]
        for num in nums[1:]:
            if num > res[-1]:
                res.append(num)
            else:
                pos = bisect.bisect_left(res, num)
                res[pos] = num
        return len(res)
