#week12-4.py
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()   # 走過的，不要再走
        path = defaultdict(list)  # path[now]與城市相接
        
        for a, b in connections:
            path[a].append((b, 1))
            path[b].append((a, -1))
        
        def helper(now):
            ans = 0  # 有幾條路「方向不對」
            visited.add(now)
            
            for k, d in path[now]:  # 城市 now 可以到城市 k, 方向是 d
                if k not in visited:
                    if d == 1:
                        ans += 1  # 要換測方向，若方向「出去」+1
                    
                    ans += helper(k)  # 函式呼叫函式，裡面會有幾條「出去」
            
            return ans
        
        return helper(0)  # 從 0 出發

