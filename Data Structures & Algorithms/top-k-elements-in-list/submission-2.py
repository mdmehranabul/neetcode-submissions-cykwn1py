class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res=[]
        freq=[[] for i in range(len(nums)+1)]
        count={}

        for n in nums:
            count[n]=1+count.get(n,0)
        
        for n,cnt in count.items():
            freq[cnt].append(n)
        print(len(freq))
        print(freq)
        for i in range(len(freq)-1,-1,-1):
            for n in freq[i]:
                res.append(n)
                if k==len(res): return res

        