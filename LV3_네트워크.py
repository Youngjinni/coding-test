def solution(n, computers):
    answer = 0
    visited = [False] * n
    def dfs(idx):
        visited[idx] = True
        
        for conn in range(n):
            if computers[idx][conn] == 1 and not visited[conn]:
                dfs(conn)
                

    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer+=1
    return answer
#깊이 우선 탐색으로 구현했다
