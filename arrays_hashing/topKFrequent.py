import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """ 
        Problem : https://leetcode.com/problems/top-k-frequent-elements/
        1. bucket sort:
        space complexity : O(n)
        time complexity : O(n) 
        approach :
        First, use a dict to keep track of frequency of all numbers. 
        Then, use an array with length of max frequency to store numbers with different frequency. 
        Finally, we retrieve top k most frequent numbers.
        2. heap:
        space complexity : O(n)
        time complexity : O(n log n) 
        approach :
        First, use a dict to keep track of frequency of all numbers. 
        Then, use heap to find and output top k most frequent numbers. 
        """
        # bucket sort
        memory = {}
        max_freq = 0
        for num in nums:
            memory[num] = memory.get(num, 0) + 1
            if memory[num] > max_freq:
                max_freq = memory[num]
        bucket = [[] for _ in range(max_freq+1)]
        for num, amount in memory.items():
            bucket[amount].append(num)
        res = []
        for i in range(max_freq, -1, -1):
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        #heap
        memory = {}
        for num in nums:
            memory[num] = memory.get(num, 0) + 1
        heap = []
        for num in memory:
            heapq.heappush(heap, ( - memory[num] , num ))
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
