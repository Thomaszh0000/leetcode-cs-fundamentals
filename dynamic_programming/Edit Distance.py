class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        n = length of word1
        m = length of word2
        problem : https://leetcode.com/problems/edit-distance/
        2D array : 
        time complexity : O(n * m)
        space complexity : O(n * m)
        approach : 
        Create a (m + 1) * (n + 1) array dp, dp[i][j] represents minimum steps we need to convert word1[0:j] to word2[0:i]. 
        Therefore, dp[0][i] will be initialized to i and dp[i][0] to i. 
        We will iterate the 2D array from top to bottom, left to right; 
        for dp[i][j], if word2[i-1] equals to word1[j-1], we will set dp[i][j] to dp[i-1][j-1] (since two characters are the same, 
        there's no need to do any thing); 
        otherwise, we will set it to 1 plus the smallest among dp[i][j-1] (insert an character in the end of word1), 
        dp[i-1][j] (delete the character in the end of word1), dp[i-1][j-1] (replace the character in the end of word1 with that of word2).
        Finally, we will return the answer dp[-1][-1].
        1D array :
        time complexity : O(n * m)
        space complexity : O(min(n, m))
        The only difference is that we use a 1D array dp (initialized to [0,...,n] if the length of word1 is smaller and [0,...,m] otherwise to save space) to store the current iteration value. 
        We use a outer for-loop to iterate from 1 to m (word2) and inner for-loop to iterate from 1 to n (word1). 
        While it is iterated to i in outer for-loop, we will set an interger prev (stores the upper-left value from the previous row) to i-1 and dp[0] to i. 
        For j in [1,n], we will save the current value as temp (use as prev for the next iteratoin); 
        if word1[j-1] is same as word2[i-1], we will set it as prev (the upper-left one); 
        otherwise, set it to min(dp[j-1] (the left one), dp[j] (the upper one), prev (the upper-left one)) + 1.
        Finally, return the answer dp[-1].
        """
        #2D ARRAY
        l1 = len(word1)
        l2 = len(word2)
        dp = [[0 for _ in range(l1 + 1)] for _ in range(l2 + 1)]
        for i in range(l1 + 1):
            dp[0][i] = i
        for i in range(l2 + 1):
            dp[i][0] = i
        for i in range(1, l2 + 1):
            for j in range(1, l1 + 1):
                if word2[i - 1] == word1[j - 1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        return dp[-1][-1]
        #1D ARRAY
        l1 = len(word1)
        l2 = len(word2)
        if l1 > l2:
            word1, word2 = word2, word1
            l1, l2 = l2, l1
        dp = [i for i in range(l1 + 1)]
        for i in range(1, l2 + 1):
            prev = i - 1
            dp[0] = i
            for j in range(1, l1 + 1):
                temp = dp[j]
                if word1[j - 1] == word2[i - 1]:
                    dp[j] = prev
                else:
                    dp[j] = min(dp[j-1], dp[j], prev) + 1
                prev = temp
        return dp[-1]
