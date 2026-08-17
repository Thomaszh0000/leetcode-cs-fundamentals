class Solution:
    """
    space complexity : will be exponential in worst case (output-sensitive).
    time complexity : will be exponential in worst case (output-sensitive).
    problem : 
    https://leetcode.com/problems/combination-sum/
    approach :
    Create a DP array with length target + 1.
    dp[i] store all combinations that can extend the current sum i to reach the target.
    Then process each candidate and iterate backward (from dp[target] to dp[0]). Process iteration of candidates in outer loop, iteration of DP in inner loop to ensure consistent candidate order, avoiding duplicate combinations.
    If candidate + i <= target, add all combinations stored in dp[i + candidate] for all candidates to dp[i]. (dp[-1] will therefore be initialized to empty combination)
    Finally, dp[0] will be our answer.
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]
        dp[-1] = [[]]
        for candidate in candidates:
            for i in range(len(dp) - 2, -1, -1):
                if i + candidate <= target:
                    for memo in dp[i + candidate]:
                        dp[i].append(memo + [candidate])
        return dp[0]
