class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        mem = defaultdict(list)
        for x, y in edges:
            # 양쪽으로 방향
            mem[x].append(y)
            mem[y].append(x)
            
        def DFS(node, end, visited):
            if node == end:
                return True
            if node in visited: # 이미 방문한 노드이면 False
                return False
            
            visited.add(node)
            for n in mem[node]: # 0 의 방향모두
                if DFS(n, end, visited): # end 를 찾으면
                    return True
                # 못찾으면 다음 루프
            
            # 모든 루프에서 못찾으면 False
            return False
            
        
        visited = set()
        return DFS(source, destination, visited)