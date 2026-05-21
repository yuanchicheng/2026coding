class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)  # 先知道有幾個 Nodes
        visited = set()  # 走過的地方，不要再走

        def helper(now):  # 函式呼叫式，因為 function stack 就是一種 DFS
            visited.add(now)

            for k in range(N):
                if k not in visited and isConnected[now][k]:
                    helper(k)

        ans = 0  # 有幾群，是相連的

        for i in range(N):  # 全部 node 巡一次
            if i not in visited:  # 若有走過的話
                ans += 1  # 代表新的一群
                helper(i)  # 函式呼叫式，表示把它的鄰居、鄰居的鄰居、...全部走過

        return ans

