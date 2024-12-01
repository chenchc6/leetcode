from collections import deque, defaultdict

class Solution:
    def networkBecomesIdle(self, edges, patience):
        n = len(patience)  # Number of servers

        # Step 1: Build graph as an adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Step 2: Compute shortest path from master server (node 0) to all servers using BFS
        dist = [-1] * n  # Distance array, initialized to -1 (unvisited)
        dist[0] = 0  # Master server has distance 0
        queue = deque([0])  # BFS queue

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if dist[neighbor] == -1:  # If not visited
                    dist[neighbor] = dist[node] + 1
                    queue.append(neighbor)

        # Step 3: Calculate the time when the network becomes idle
        max_idle_time = 0
        for i in range(1, n):  # Skip the master server (node 0)
            round_trip_time = 2 * dist[i]
            last_resend_time = (round_trip_time - 1) // patience[i] * patience[i]
            idle_time = last_resend_time + round_trip_time
            max_idle_time = max(max_idle_time, idle_time)

        # Step 4: Return the maximum idle time + 1 (network becomes idle at the start of the next second)
        return max_idle_time + 1