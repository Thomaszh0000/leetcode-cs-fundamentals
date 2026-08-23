class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        n = length of grid[0]
        m = length of grid
        time complexity : O(n * m)
        space complexity : O(n * m) because of recursion
        problem : https://leetcode.com/problems/number-of-islands/?source=submission-noac
        approach : 
        Define a function dfs(y,x), which will check whether grid[y][x] is "0"; 
        if it is "0", the function will be exited; if it is "1", 
        the function will then change grid[y][x] from "1" to "0". 
        After that, the function will check if y > 0, then execute dfs(y - 1, x); if y < m - 1, dfs(y + 1, x); if x > 0, dfs(y, x - 1); if x < n - 1, dfs(y, x + 1). Therefore, if we are sure there's one element in grid that is "1", we will then add one to our result and eliminate the whole island we encountered. After iterating the function through the whole grid (if grid[y][x] is "1", add 1 to result and execute dfs(y,x)), we will then return our result.
        """
        n, m = len(grid[0]), len(grid)
        count = 0
        def dfs(y,x):
            if grid[y][x] == "0":
                return
            if grid[y][x] == "1":
                grid[y][x] = "0"
            if y > 0:
                dfs(y - 1, x)
            if y < m - 1:
                dfs(y + 1, x)
            if x > 0:
                dfs(y, x - 1)
            if x < n - 1:
                dfs(y, x + 1)
        for y in range(m):
            for x in range(n):
                if grid[y][x] == "1":
                    count += 1
                    dfs(y,x)
        return count
