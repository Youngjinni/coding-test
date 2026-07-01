from collections import deque

def solution(storage, requests):
    n = len(storage)
    m = len(storage[0])
    
    board = [['.'] * (m + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(m):
            board[i + 1][j + 1] = storage[i][j]
            
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    for req in requests:
        target = req[0]
        
        if len(req) == 2:
            for r in range(1, n + 1):
                for c in range(1, m + 1):
                    if board[r][c] == target:
                        board[r][c] = '.'
                        
        else:
            q = deque([(0, 0)])
            visited = [[False] * (m + 2) for _ in range(n + 2)]
            visited[0][0] = True
            
            targets_to_remove = []
            
            while q:
                r, c = q.popleft()
                
                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    
                    if 0 <= nr < n + 2 and 0 <= nc < m + 2:
                        if not visited[nr][nc]:
                            if board[nr][nc] == '.':
                                visited[nr][nc] = True
                                q.append((nr, nc))
                            elif board[nr][nc] == target:
                                visited[nr][nc] = True
                                targets_to_remove.append((nr, nc))
                                
            for r, c in targets_to_remove:
                board[r][c] = '.'

    answer = 0
    for r in range(1, n + 1):
        for c in range(1, m + 1):
            if board[r][c] != '.':
                answer += 1
                
    return answer
  #collections라이브러리에 대해 더 알아봐야겠다
