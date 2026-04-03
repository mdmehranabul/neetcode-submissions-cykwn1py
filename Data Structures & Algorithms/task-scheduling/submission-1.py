class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        t=0
        count = Counter(tasks)
        Heap = [-n for n in count.values()]
        heapq.heapify(Heap)
        q= deque()

        while q or Heap:
            t+=1
            if Heap:
                val = 1+heapq.heappop(Heap)
            
                if val!=0:
                    q.append((val,t+n))
            
            
            if q and q[0][1]==t:
                task,time=q.popleft()
                heapq.heappush(Heap,task)
        return t
            

            
