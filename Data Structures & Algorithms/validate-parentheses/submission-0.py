class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            "}": "{",
            "]": "[",
            ")": "("
            }

        stack = []

        for p in s:
            if p in dic:
                if stack and stack[-1] == dic[p]:
                    stack.pop()
                else: 
                    return False
            else:
                stack.append(p)
        
        return True if not stack else False