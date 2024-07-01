class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        
        hashMap = {}

        def dfs(cur, color):
            if cur in hashMap:
                return False if hashMap[cur] != color else True
            hashMap[cur] = color
            for neighbour in graph[cur]:
                if not dfs(neighbour, not color):
                    return False
            return True

        for i in range(len(graph)):
            if not dfs(i, hashMap.get(i, 0)):
                return False


        return True