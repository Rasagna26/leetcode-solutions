class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
            n = len(graph)
            rev = [[] for i in range(n)]
            outd = [0] * n
            q=[]
            vis = [False] * n
            for u in range(n):
                for v in graph[u]:
                    rev[v].append(u)
                    outd[u]+=1
            for i in range(n):
                if outd[i] == 0:
                    q.append(i)
           
            while q:
                node = q.pop(0)
                vis[node] = True
                
                for nei in rev[node]:
                    outd[nei] -= 1
                    if outd[nei] == 0:
                        q.append(nei)
            
            return [i for i in range(n) if vis[i]]
