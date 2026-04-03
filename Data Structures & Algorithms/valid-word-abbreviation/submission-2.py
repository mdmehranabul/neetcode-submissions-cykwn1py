class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i,j = 0,0

        while i<len(word) and j<len(abbr):
            if word[i]==abbr[j]:
                i,j=i+1,j+1
            elif abbr[j].isalpha() or abbr[j]=="0":
                return False
            else:
                sublen=0
                
                while j<len(abbr) and not abbr[j].isalpha():
                    sublen = 10*sublen + int(abbr[j])
                    j+=1
                i=i+sublen
        return True if (i == len(word) and j == len(abbr)) else False

# Time Complexity - O(m+n)
# Space Complexity - O(1)