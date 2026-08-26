class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        n = length of s
        Space complexity : O(1)
        Time complexity : O(n)
        problem : https://leetcode.com/problems/valid-palindrome/
        approach :
        We create two pointers left and right, and initialize them to 0 and n - 1 separately.
        Use while-loop (outer while loop) : while left < right -> while left < right (inner while loop) and not (ord("0") <= ord(s[left]) <= ord("9")) and not (ord("a") <= ord(s[left]) <= ord("z")) and not (ord("A") <= ord(s[left]) <= ord("Z")), we will add one to left (we wrote ord("0") <= ord(s[left]) <= ord("9") to ensure that s[left] is any of 0 - 9, same idea of ord("a") <= ord(s[left]) <= ord("z") and ord("A") <= ord(s[left]) <= ord("Z")); after that, we are sure that s[left] is an alphanumeric character. We then do same thing to right; then we compare s[left].lower() and s[right].lower(), if they are the same, increment left and decrement right (to move forward and prevent infinite loop); if it is not, return False.
        If we break the outer while, it means we've checked all Alphanumeric characters, so we will then return True.
        Note :
        We can also use isalnum(), which is implemented in C and is generally faster.
        """
        n = len(s)
        left, right = 0, n-1
        while left < right:
            while left < right and not (ord("0") <= ord(s[left]) <= ord("9")) and not (ord("a") <= ord(s[left]) <= ord("z")) and not (ord("A") <= ord(s[left]) <= ord("Z")):
                left += 1
            while left < right and not (ord("0") <= ord(s[right]) <= ord("9")) and not (ord("a") <= ord(s[right]) <= ord("z")) and not (ord("A") <= ord(s[right]) <= ord("Z")):
                right -= 1
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False

        return True
