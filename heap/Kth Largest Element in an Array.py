import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        n = length of nums
        time complexity : O(n * log k)
        space complexity : O(k)
        problem : https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/2118887797/
        Keep track of a heap array "heap" of maximum length k. For num in nums, 
        if the length of heap is smaller than k (hasn't reached the maximum), 
        we will push num to heap; if the length equals to k (so if there's new element can be push inside, we need to pop out the smallest one), 
        if num > heap[0] (the smallest one), we will pop out heap[0] and push num to heap (so we will always keep track of the k largest numbers so far).
        Finally, we will return our answer, heap[0].
        """
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                if num > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)
        return heap[0]
