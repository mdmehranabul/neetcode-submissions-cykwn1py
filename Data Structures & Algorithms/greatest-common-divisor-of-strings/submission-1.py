class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        def divisor(l):
            if len(str1)%l or len(str2)%l:
                return False
            f1,f2 = len(str1)//l,len(str2)//l
            return str1[:l]*f1 == str1 and str1[:l]*f2 == str2
            
        
        for l in range(min(len(str1),len(str2)),0,-1):
            if divisor(l):
                return str1[:l]
        return ""

        