class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]

        for key,value in enumerate(temperatures):
            while stack and value>stack[-1][0]:
                stack_val,stack_key=stack.pop()
                res[stack_key]=key-stack_key
            stack.append([value,key])
        return res