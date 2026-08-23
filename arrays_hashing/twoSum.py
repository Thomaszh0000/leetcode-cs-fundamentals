class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        space complexity : O(n)
        time complexity : O(n)
        Problems :
        https://leetcode.com/problems/two-sum/
        Approach : 
        Using hashtable to store complement of each element ( target - element ) along with its index. For each element,
        check whether it is already in the hashtable; if it is, it means we have found two indices we want.
        """
        seen = {}
        for i, num in enumerate(nums):
            if num in seen:
                return [seen[num], i]
            else:
                seen[target - num] = i
              
