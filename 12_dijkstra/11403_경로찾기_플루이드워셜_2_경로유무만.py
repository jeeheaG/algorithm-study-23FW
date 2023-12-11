# https://www.acmicpc.net/problem/11403
# 모든 정점 -> 플루이드
# 경로가 존재하는지만 알면 됨

from sys import stdin
input = stdin.readline

## 입력
n = int(input()) #노드개수

#경로 존재여부
board=[]
for _ in range(n) :
    board.append(list(map(int, input().split())))

## 풀이 : 플루이드 워셜, 경로가 존재하는지만 확인
for k in range(n) :
    for a in range(n) :
        for b in range(n) :
            # 거쳐가는 경로가 존재한다면 갱신
            if board[a][k]==1 & board[k][b]==1 :
                board[a][b] = 1

## 출력
for b in board :
    print(*b)