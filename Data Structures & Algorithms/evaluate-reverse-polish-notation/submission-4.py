class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        calc=0
        for t in tokens:
            if t == "*":
                b, a = stack.pop(), stack.pop()
                calc = a*b
                stack.append(calc)
            elif t == "+":
                b, a = stack.pop(), stack.pop()
                calc = a+b
                stack.append(calc)
            elif t == "-":
                b, a = stack.pop(), stack.pop()
                calc = a-b
                stack.append(calc)
            elif t == "/":
                b, a = stack.pop(), stack.pop()
                calc = int(a/b)
                stack.append(calc)
            else:
                stack.append(int(t))
        return stack[0]

# Time Complexity - O(n)
# Space Complexity - O(n)



        