class Solution:
    def reverse(self, x: int) -> int:
        MAX,MIN=2**31-1,-2**31
        rev=0
        while x:
            rem=int(math.fmod(x,10))
            x=int(x/10)

            if (rev > MAX//10) or (rev==MAX//10 and rem>MAX%10):
                return 0
            
            if (rev<MIN//10) or (rev==MIN//10 and rem<8):
                return 0
            
            rev=rev*10+rem
        return rev

        