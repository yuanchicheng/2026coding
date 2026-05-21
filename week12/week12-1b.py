#week12-1b.py
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        
        def helper(now):  # 函式呼叫函式的版本，也能進行DFS
            for k in rooms[now]:
                if k not in visited:
                    visited.add(k)
                    helper(k)
        
        visited.add(0)
        helper(0)
        
        return len(rooms) == len(visited)

