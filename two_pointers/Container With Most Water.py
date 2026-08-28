class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        n = length of the array height
        time complexity : O(n)
        space complexity : O(1)
        problem : https://leetcode.com/problems/container-with-most-water/
        approach :
        Keep track of two pointers left and right initialized to 0 and n - 1 separately and one integer best initialized to (n - 1) * min(height[left], height[right]).
        Use a while-loop : while left < right, if height[left] < height[right], increment left; otherwise, decrement right; we then update best using max(best, (right - left) * min(height[right], height[left])).
        Finally, we return our result best.
        note : 
        Here prove why this algorithm works :
        Proof of Contradiction ->
        W.L.O.G. let height[i] <= height[j] and the optimal solution be (i, j) such that area(i, j) = OPT = (j - i) * height[i] (height[i] <= height[j]).
        (Rule)We would like to prove in any step before we met the solution, either left should < i or right > j (that is, left <= i and right >= j and (left, right) != (i, j)).
        (1) If now height[left] <= height[right] and left = i (so after this step left would be i + 1 and break our rule), since left = i, right should > j; now we can se that area(i, right) = (right - i) * height[i] > OPT *** CONTRADICTION.
        (2) If now height[left] > height[right] and right = j (so after this step right would be j - 1 and break our rule), since right = j, left should < i; now we can se that area(left, j) = (j - left) * height[j] > OPT *** CONTRADICTION.
        Therefore in any steps before we met the solution, left <= i and right >= j and (left, right) != (i, j), so we can definitely met the solution by this algorithm.
        ### QED
        """
        n = len(height)
        left, right = 0, n - 1
        best = (n - 1) * min(height[left], height[right])
        while left < right:
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            best = max(best, (right - left) * min(height[right], height[left]))
        return best
