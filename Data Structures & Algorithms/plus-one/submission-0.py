class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        one=1
        i = 0 

        while one and i < len(digits):
            if digits[i]==9:
                digits[i]=0
            else:
                digits[i]+=1
                one = 0
            i+=1

        if one:
            digits.append(one)
        
        return digits[::-1]


        