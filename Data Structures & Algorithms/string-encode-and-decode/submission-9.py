class Solution:

    def encode(self, strs: List[str]) -> str:
        
        res=""

        for s in strs:
            res+=str(len(s))+"#"+s
        
        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        # 5#Hello5#World

        i = 0
        res=[]
        while i<len(s):
            j = i
            while s[j]!="#":
                j+=1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            res.append(word)
            i = j+1+length
        return res

# Time Complexity : O(m)
# Space Complexity : O(m + n)
# m is the sum of lengths of all the strings and n is the number of strings.

