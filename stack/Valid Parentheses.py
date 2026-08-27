class Solution:
    def isValid(self, s: str) -> bool:
        """
        time complexity : O(n)
        space complexity : O(n)
        problem : https://leetcode.com/problems/valid-parentheses/
        approach :
        Use a dict "convert" to store the mapping relationship between '({[' and ')}]',
        then keep track of an array stack.
        Use a for-loop : for c in s, if c equals to any of "[" or "(" or "{", append c to the back of stack; 
        if it is not, if stack is not empty (to prevent the situation that the number of close brackets are more than that of open brackets) and stack.pop() equals to convert[c],
        continue, otherwise, return False.
        After iteration, if stack is [], return True, else return False (means there're open brackets left).
        """
        convert = {"}":"{", "]" : "[", ")" : "("}
        stack = []
        for c in s:
            if c in '[({':
                stack.append(c)
            else:
                if stack and stack.pop() == convert[c]:
                    continue
                else:
                    return False
        if not stack:
            return True
        else:
            return False
