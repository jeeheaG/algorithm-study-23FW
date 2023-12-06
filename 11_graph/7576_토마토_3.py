# https://www.acmicpc.net/problem/7576
# 그래프 -> 2차원배열 or 딕셔너리
# bfs -> 큐deque
# 대박 날짜대로 익어야되니까 bfs 맞네맞아...날짜가 depth.. depth깊어질 때 visited초기화, 날짜수카운트(또는 최대값 가져옴)
# Aㅏ.... 나 문제 잘못 이해하고 있었음...^^.. 익은 토마토는 다음날까지만 다른 토마토를 익힐 수 있음..당연함..하루이상 지나면 주변에 또 익힐 토마토가 없음...... 앞으론 종이에 그리면서 풀어라 메모장에 시뮬하던가
# ?) 방문체크 왜 안해도 되는지 다시한번 풀어보기 

from collections import deque
from sys import stdin
input = stdin.readline

## 입력
c, r = map(int, input().split())

#토마토상자입력, 익은토마토 찾아서 큐에 담기(시작점)
board = []
que = deque()
for i in range(r) :
    arr = list(map(int, input().split()))
    board.append(arr)
    for j in range(c) :
        if arr[j]==1 :
            que.append((i, j))


# #토마토 상자
# board = []
# for i in range(r) :
#     board.append(list(map(int, input().split())))

# #bfs에 쓸 큐
# que = deque()

# #익은 토마토 찾아서 큐에 담기(시작점)
# for i in range(r) :
#     for j in range(c) :
#         if(board[i][j]==1) :
#             que.append((i,j))

#방향 노드 상하좌우
direc_arr = [(1, 0), (-1, 0), (0, -1), (0, 1)]


## 풀이 : bfs 토마토 익히기
day = -1 #처음 익어있는 토마토를 익히는 반복횟수는 카운트 제외
que_2 = deque() # 다음날 주변익힐 토마토 킵
while que or que_2 : 
    # print("next day que : ", *que)
    # visited = [[False] * (c) for _ in range(r)]
    while que :
        cur = que.popleft()

        for direc in direc_arr :
            nr, nc = cur[0] + direc[0], cur[1] + direc[1] #위치 한칸 이동

            #칸을 벗어나거나, 토마토가 없는 칸이거나, 
            #이미 이날 익힌 토마토거나, 이미 익었던 토마토면 인접토마토 탐색 안하고 넘어감
            if nr < 0 or r <= nr or nc < 0 or c <= nc or board[nr][nc]==-1 or \
                board[nr][nc]==1 : #visited[nr][nc] or 
            # if not (0 <= nr < r and 0 <= nc < c and not visited[nr][nc] and board[nr][nc]==0) :
                continue
            
            #방문 체크
            # visited[nr][nc] = True
            #인접토마토를 익히고
            board[nr][nc] +=1
            #방금 익힌 인접토마토를 다음날 탐색할 큐에 킵
            que_2.append((nr, nc))

    que = que_2.copy()
    que_2.clear() # = deque()로 아예 확실하게 새로 해줄 수도 있음
    day +=1 # 하루 지남

# for b in board :
#     print(*b)

isDone = True
for row in board :
    for r in row :
        if r==0 : isDone = False

print(day if isDone else -1)




