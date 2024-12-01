from collections import defaultdict
from typing import List

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # Map to store email -> name mapping
        email_to_name = {}
        # Adjacency list to represent the graph
        graph = defaultdict(set)

        # Build the graph and the email-to-name mapping
        for account in accounts:
            name = account[0]
            first_email = account[1]
            for email in account[1:]:
                email_to_name[email] = name
                # Add edges to the graph (undirected)
                graph[email].add(first_email)
                graph[first_email].add(email)

        # DFS function to find all emails in a connected component
        def dfs(email, component):
            visited.add(email)
            component.append(email)
            for neighbor in graph[email]:
                if neighbor not in visited:
                    dfs(neighbor, component)

        visited = set()
        result = []

        # Perform DFS for each email
        for email in graph:
            if email not in visited:
                component = []
                dfs(email, component)
                # Sort emails and prepend the name
                result.append([email_to_name[email]] + sorted(component))

        return result