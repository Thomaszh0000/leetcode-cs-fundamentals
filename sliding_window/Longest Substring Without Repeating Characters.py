class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        n = length of s
        space complexity : O(min(n, number of all characters))
        time complexity : O(n)
        problem : https://leetcode.com/problems/longest-substring-without-repeating-characters/
        If length of s is 0, we will just return 0.
        Otherwise, we will use an integer maxL initialized to 1 to keep track of answer, 
        two pointers l(left), 
        r(right) used to keep track of the answer window and a dict "seen" initialized to {s[0] : 0} to keep track of the most recent index of each character.
        Use a for-loop : for r in [1,n-1], 
        if s[r] is in seen and l <= seen[s[r]] (we use this condition to prevent edge cases like "bccccccb" : 
        while l = 6, r = 7, since seen["b"] will be 0 at this time, this will move l to 1 and give the wrong answer 7), 
        we will move l to seen[s[r]] + 1 and set seen[s[r]] to r; we will then calculate the maximum maxL.
        After iteration of the for-loop, we will then return answer maxL.
        """
        if not s:
            return 0
        n = len(s)
        maxL = 1
        l, r = 0, 0
        seen = {s[0] : 0}
        for r in range(1,n):
            if s[r] in seen and l <= seen[s[r]]:
                l = seen[s[r]] + 1
            seen[s[r]] = r
            maxL = max(maxL, r - l + 1)
        return maxL
