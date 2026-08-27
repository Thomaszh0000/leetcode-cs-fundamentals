class Solution:
    def characterReplacement(self, s: str, k: int) -> int :
        """
        n = length of s
        time complexity : O(n)
        space complexity : O(1)
        approach : 
        Window :
        Keep track of four integers, max_count (the highest frequent character's frequency in window so far), left (left edge of window), right (right edge of window) and best (answer) and one dict "count" used to keep track of frequency of each character in the window.
        Use a for-loop, for right in [1,n-1], add 1 to count[s[right]] (if it does not exist, set it to 1); then if max_count < count[s[right]], set max_count to count[s[right]]; if right - left + 1 - max_count > k, minus one to count[s[left]] and increment left; we will then update best using max(best, right - left + 1).
        Finally, after iteration, we will return our answer best.
        note : the reason we only need to keep track of the biggest max_count so far is that if s[right] equals to the character max_count represents, it will update the answer; if it is not, then s[left] will be discard, and the answer wouldn't be changed. We will only change the max_count if we encounter other charater representing max_count or there is any other character has higher frequency than the current one, that is, we want to create the biggest answer using max_count.
        """
        n = len(s)
        max_count = 1
        left = 0
        best = 1
        count = {s[0] : 1}
        for right in range(1, n) :
            count[s[right]] = count.get(s[right], 0) + 1
            if max_count < count[s[right]] :
                max_count = count[s[right]]
            if right - left + 1 - max_count > k :
                count[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best
