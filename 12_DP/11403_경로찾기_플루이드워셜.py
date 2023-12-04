# 모든 노드 간의 경로에 대한 문제 -> 플루이드 워셜
# 궁금) 플루이드는 최단경로를 구해주는데 최단경로라는 조건이 필요없는 다른 풀이법은 없나?
# -> A) 없다고 보면 된다!! 그냥 암기 >> 모든경로, 모든 정점에서 모든 정점 = 플로이드
from sys import stdin
input = stdin.readline

## 입력
n = int(input()) #노드개수

#간선 입력, 최단경로 테이블
board = [[] for _ in range(n)] # 가로세로 입력받기 복잡해서 n+1말고 그냥 n으로 씀
for i in range(n) :
     # ?이렇게 밖에 입력 못받나? 간선이 없어0인 경우 inf로 넣어라
    arr = list(map(int, input().split()))
    for j in range(n) :
        if(arr[j]==0) :
            arr[j] = float("inf")
    board[i] = arr

# print(*board, sep="\n")


## 풀이 : 플루이드워셜
for k in range(n) :
    for a in range(n) :
        for b in range(n) :
            board[a][b] = min(board[a][b], board[a][k]+board[k][b])

# print(*board, sep="\n")

## 출력
for i in range(n) :
    for j in range(n) :
        if board[i][j] == float("inf") :
            board[i][j] = 0
        else :
            board[i][j] = 1
    print(*board[i])