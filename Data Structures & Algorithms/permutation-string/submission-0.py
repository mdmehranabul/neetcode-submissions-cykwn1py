class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2): return False
        hash_s1=[0]*26
        hash_s2=[0]*26

        for i in range(len(s1)):
            hash_s1[ord(s1[i])-ord('a')]+=1
            hash_s2[ord(s2[i])-ord('a')]+=1

        l=0
        for r in range(len(s1),len(s2)):
            if hash_s1==hash_s2:
                return True

            hash_s2[ord(s2[r])-ord('a')]+=1
            hash_s2[ord(s2[l])-ord('a')]-=1

            l+=1
        return hash_s1==hash_s2