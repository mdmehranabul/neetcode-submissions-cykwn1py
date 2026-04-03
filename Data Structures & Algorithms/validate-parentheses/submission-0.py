class Solution:
    def isValid(self, s: str) -> bool:
        hashset={"]":"[","}":"{",")":"("}
        stack=[]
        
        for c in s:
            if c in hashset:
                if stack and stack[-1]==hashset[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return False if stack else True