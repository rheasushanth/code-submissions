class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):

        INF = float('inf')

        dist = [INF] * n
        dist[src] = 0

        # At most k stops = k + 1 flights
        for _ in range(k + 1):

            temp = dist[:]

            for u, v, price in flights:

                if dist[u] != INF:

                    temp[v] = min(
                        temp[v],
                        dist[u] + price
                    )

            dist = temp

        return -1 if dist[dst] == INF else dist[dst]