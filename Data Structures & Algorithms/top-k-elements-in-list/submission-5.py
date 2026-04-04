class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map={}
        freq_map=[[] for i in range(len(nums)+1)]

        for n in nums:
            hash_map[n]=1+hash_map.get(n,0)
        for n, f in hash_map.items():
            freq_map[f].append(n)

        res = []
        print(freq_map)
        for i in range(len(freq_map)-1,-1,-1):
            for n in freq_map[i]:
                res.append(n)
                if len(res)==k : return res


# Time Complexity - O(n)
# Space Complexity - O(n)