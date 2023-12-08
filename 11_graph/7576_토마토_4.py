# https://www.acmicpc.net/problem/7576
# 한번 더 풀기
# 2차원배열, 최소일수 -> bfs -> 큐deque

from collections import deque
from sys import stdin
input = stdin.readline

## 입력
c, r = map(int, input().split())

#토미토박스, 익은토마토 bfs큐에 담음
que = deque()
board = []
for i in range(r) :
    arr = list(map(int, input().split()))
    board.append(arr)
    for j in range(c) :
        if arr[j]==1 :
            que.append((i,j))

# print(*board, sep="\n")

#방향노드 상하좌우
dir = [(1,0), (-1,0), (0,-1), (0,1)]

# 풀이 : bfs
#날짜(depth) 세야함
day = -1
while que :
    que_2 = deque()

    while que : 
        cr, cc = que.popleft()

        for dr, dc in dir :
            nr, nc = cr+dr, cc+dc
            
            #인접노드를 탐색하지 않아야 하는 조건
            #인덱스벗어남, 토마토 없음(-1), 토마토 이미 익었었음(1)
            if not (0 <= nr < r and 0 <= nc < c) or board[nr][nc]==-1 or board[nr][nc]==1 :
                continue
                
            #인접노드 탐색(익히기)
            board[nr][nc] = 1
            que_2.append((nr,nc))

    que = que_2
    day +=1

## 출력
isDone = True
for row in board :
    for val in row :
        if val==0 : isDone = False

print(day if isDone else -1)
