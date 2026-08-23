class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        n = numCourses
        m = length of prerequisites
        space complexity : O(n + m)
        time complexity : O(n + m)
        problem :　https://leetcode.com/problems/course-schedule/
        approach :
        Create an array "prereq" such that prereq[course] stores all prerequisities of course.
        Then Keep track of an array "states" used to keep track of status of each course while checking : 0 means not checked, 1 means being checked, 2 means already checked.
        We will then define a function dfs(course) used to check whether a course is possible to be taken or not; if states[course] eqauls to 1 (this means the course is already in current DFS path, which means a cycle), we will return False.
        If states[course] equals to 2, we will then return True (it is possible to take this course); if states[course] equals to 0, we will set states[course] to 1 and for each crs (we use another name "crs" to prevent misundertood) in prereq[course], if dfs(crs) eqauls to False (the function will check whether crs is able to be taken), it will return False; after checking all crs, states[course] will be set to 2 (has been checked) and return True (after checking, we are sure that this course could be taken).
        Finally, we execute dfs(crs) for crs in [0, numCourses-1] to check whether each course could be taken (actually, some will already be checked while we are checking the previous ones, and the function will return True without any futher step); if we pass all scrutiny, return True.
        """
        states = [0] * numCourses
        prereq = {i : set() for i in range(numCourses)}
        for crs, req in prerequisites:
            prereq[crs].add(req)
        def dfs(course):
            if states[course] == 1:
                return False
            if states[course] == 2:
                return True
            states[course] = 1
            for crs in prereq[course]:
                if not dfs(crs):
                    return False
            states[course] = 2
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
