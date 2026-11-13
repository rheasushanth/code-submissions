class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        graph = defaultdict(list)
        for (a,b,d) in roads:
            graph[a].append((b,d))
            graph[b].append((a,d))
        visited = {1}
        q = deque([1])
        ans = float('inf')
        while q:
            node = q.popleft()
            for nei, d in graph[node]:
                ans = min(ans, d)
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)
        return ans

            


        