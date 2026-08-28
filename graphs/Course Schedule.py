from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        n = numCourses
        m = length of prerequisites
        space complexity : O(n + m)
        time complexity : O(n + m)
        problem : https://leetcode.com/problems/course-schedule/
        approach :
        Create an array "prereq" such that prereq[course] stores all prerequisites of course.
        Then keep track of an array "states" used to store the status of each course:
        0 means not checked, 1 means being checked, and 2 means already checked.
        If DFS reaches a course with state 1, that means there is a cycle.
        After checking all prerequisite paths for one course, mark it as state 2.
        Finally, run DFS for every course. If no cycle is found, all courses can be finished.
        """
        states = [0] * numCourses
        prereq = {i: set() for i in range(numCourses)}
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
