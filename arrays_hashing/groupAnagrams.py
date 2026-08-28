from typing import List


class Solution:
    """
    m = average length of strings
    n = length of list "strs"
    time complexity : O(n * m)
    space complexity : O(n)
    Problem:
    https://leetcode.com/problems/group-anagrams/
    Approach:
    For each word in list "strs", count the frequency of each character using an array of length 26.
    Convert the array to tuple so it can be used as a hashable dictionary key.
    Anagrams need to have the same character frequency, so strings with the same frequency go to the same group.
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        convert = {}
        res = []
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord("a")] += 1
            count = tuple(count)
            if count not in convert:
                convert[count] = len(res)
                res.append([string])
            else:
                res[convert[count]].append(string)
        return res
