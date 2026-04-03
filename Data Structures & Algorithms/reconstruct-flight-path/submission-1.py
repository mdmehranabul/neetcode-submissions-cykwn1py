class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # hashmap={src:[] for src, dst in tickets}
        # tickets.sort()

        # for src,dst in tickets:
        #     hashmap[src].append(dst)

        
        # res=["JFK"]

        # def dfs(src):
        #     if len(res)==len(tickets)+1: return True
        #     if src not in hashmap: return False

        #     temp=hashmap[src]
        #     for i,v in enumerate(temp):
        #         hashmap[src].pop(i)
        #         res.append(v)
        #         if dfs(v): return True
        #         hashmap[src].insert(i,v)
        #         res.pop()
        # dfs("JFK")
        # return res


        hashmap=defaultdict(list)
        tickets.sort(reverse=True)
        res=[]
        for src,dst in tickets:
            hashmap[src].append(dst)
        print(hashmap)

        def dfs(node):
            while hashmap[node]:
                dfs(hashmap[node].pop())
            res.append(node)
        
        dfs("JFK")
        return res[::-1]



        