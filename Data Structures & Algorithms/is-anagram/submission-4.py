class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # if len(s)!=len(t): return False

        # hash_s = defaultdict(int)
        # hash_t = defaultdict(int)

        # for i in range(len(s)):
        #     hash_s[s[i]]=1+hash_s.get(s[i],0)
        #     hash_t[t[i]]=1+hash_t.get(t[i],0)
        
        # for k,v in hash_s.items():
        #     if v!=hash_t[k]:
        #         return False
        # return True

# Time Complexity - O(m+n)
# Space Complexity - O(m+n) or O(26)

        if len(s)!=len(t): return False

        hash_s = defaultdict(int)
        hash_t = defaultdict(int)

        for i in range(len(s)):
            hash_s[s[i]]=1+hash_s.get(s[i],0)
            hash_t[t[i]]=1+hash_t.get(t[i],0)
        
        return hash_s == hash_t

# Time Complexity - O(m+n)
# Space Complexity - O(m+n) or O(26)
        