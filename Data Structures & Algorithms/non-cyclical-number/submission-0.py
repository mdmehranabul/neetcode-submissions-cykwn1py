class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            if n == 1: return True
            visit.add(n)

            n = self.sum_of_squares(n)
        return False
    
    def sum_of_squares(self,n):
        output=0
        while n:
            digit = n%10
            digit = digit **2
            output +=digit
            n = n//10
        return output


# Time Complexity - O(log n)
# Space Complexity - O(log n)