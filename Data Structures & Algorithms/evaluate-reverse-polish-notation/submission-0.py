class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res=0
        stack=[]

        for c in tokens:
            if c=="+":
                b,a=stack.pop(),stack.pop()
                res=a+b
                stack.append(res)
            elif c=="-":
                b,a=stack.pop(),stack.pop()
                res=a-b
                stack.append(res)
            elif c=="*":
                b,a=stack.pop(),stack.pop()
                res=a*b
                stack.append(res)
            elif c=="/":
                b,a=stack.pop(),stack.pop()
                res=int(a/b)
                stack.append(res)
            else:
                stack.append(int(c))
        return stack[0]
        