#week12-1a.py
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        stack = [0]  # 我們利用 stack 裡面有待處理的房間，一開始 房間0 是開的
        visited = set()  # 存去過、處理過的房間，不要再進去了
        visited.add(0)  # 已經拿好、等候處理，下次有拿到鑰匙，不要再放入 stack
        
        while stack:  # 只要 stack 還有東西，就繼續處理
            now = stack.pop()  # 吐出1個房間，現在要來處理
            
            for k in rooms[now]:  # 把 room now 房間裡，所有的鑰匙，都拿來檢查
                if k in visited:
                    continue  # 鑰匙 k 對應的房間 k 看過了，則再檢查
                
                # 如果走到這裡，代表沒走過、沒有處理的房間 k
                stack.append(k)  # 加入 stack 等待結構
                visited.add(k)  # 標記看過所有處理，其他人不要再排處理
        
        return len(rooms) == len(visited)  # 房間的數目，全部都參觀了，成功

