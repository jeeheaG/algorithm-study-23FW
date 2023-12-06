# https://www.acmicpc.net/problem/18352 
# 최단거리 -> bfs -> 큐deque
# 그래프 입력받기 -> 딕셔너리 또는 2차원배열

from collections import deque, defaultdict
from sys import stdin
input = stdin.readline
INF = float("inf")

## 입력
v, e, ans_dist, start = map(int, input().split())

graph = defaultdict(list)
for _ in range(e) :
    sn, en = map(int, input().split())
    graph[sn].append(en)

#최단거리 배열
dist_arr = [INF for _ in range(v+1)]

#큐, 최단거리 배열에 시작노드값 초기화
que = deque([start])
dist_arr[start] = 0

## 풀이 : bfs
while que :
    #현재노드가 될 노드 pop
    cur = que.popleft()

    #현재노드의 인접노드들 탐색
    for nxt in graph[cur] :
        #현재노드를 거쳐가는 것이 지금까지의 최단거리보다 짧을 때
        if dist_arr[cur]+1 < dist_arr[nxt] :
            #최단거리 갱신하고 인접노드가 탐색되도록 큐에 넣음
            dist_arr[nxt] = dist_arr[cur]+1
            que.append(nxt)

# print(*dist_arr)

## 출력
ans = [i for i, d in enumerate(dist_arr) if d==ans_dist]
if ans :
    print(*ans, sep="\n")
else :
    print(-1)