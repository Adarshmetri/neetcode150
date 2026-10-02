class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                task = 1 + heapq.heappop(maxHeap)
                if task:
                    q.append([task, time + n])

            while q and q[0][1] == time:
                temp = q.popleft()
                heapq.heappush(maxHeap, temp[0])
        
        return time

