from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        n = length of s
        m = length of wordDict
        L = average word length
        time complexity : O(n * m * L)
        space complexity : O(n)
        problem : https://leetcode.com/problems/word-break/
        approach : Create an array dp of length n + 1, 
        dp[i] represents if s[i:] can be segmented into words from wordDict.
        dp[n] will be initialized to True (because we need 0 word while the current index is already the last one), other will be False.
        We will iterate the array with an for-loop from n - 1 to 0. 
        If there is any of words' length k such that i + k <= n and s[i:i+k] is same as the word and dp[i+k] is True, we will then set dp[i] to True.
        Finally, we will return the answer dp[0].
        """
        n = len(s)
        dp = [False] * ( n + 1 )
        dp[n] = True
        for i in range(n - 1, -1, -1):
            for word in wordDict:
                k = len(word)
                if i + k <= n and s[i:i+k] == word and dp[i+k]:
                    dp[i] = True
                    break
        return dp[0]
