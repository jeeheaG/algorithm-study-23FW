# 그래프(시작점, 가중치있음)의 최단경로 -> 다익스트라
# !!) heapq 에 노드 튜플 넣을 때 앞값에 우선순위 적용됨!! (가중치, 노드번호)로 쓸 것!
import heapq
from sys import stdin
input = stdin.readline

## 입력
v, e = map(int, input().split()) #노드, 간선 개수
k = int(input()) #시작점

#간선 유의사항: 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음
graph = [[] for _ in range(v+1)]
for _ in range(e) :
    u, vv, w = map(int, input().split()) #u->v 간선 가중치w
    graph[u].append((w, vv)) #(vv로가는 가중치w)

#최단경로, 큐, 시작점 초기화
dist_arr = [float("inf")] * (v+1)
dist_arr[k] = 0
que = []
heapq.heappush(que, (0, k)) #그냥 생성할 때부터 이렇게 써도 됨 que = [(0, k)]

## 풀이 : 다익스트라
while que :
    dist, cur = heapq.heappop(que)

    #최단거리가 이미 구해져있으면 인접노드 탐색 안함
    if dist > dist_arr[cur] :
        continue

    #인접노드 탐색
    for nxt in graph[cur] :
        cost = dist + nxt[0] #새로운 최단거리

        #새로운 최단거리 갱신여부 확인, 갱신
        if cost < dist_arr[nxt[1]] :
            dist_arr[nxt[1]] = cost
            heapq.heappush(que, (cost, nxt[1]))

## 출력
for i in range(1, v+1) :
    if dist_arr[i] == float("inf") :
        print("INF")
    else : 
        print(dist_arr[i])


## 출력은 이렇게도 가능. 같은뜻
# for i in range(1, v+1) :
#     dist = dist_arr[i]
#     print(dist if dist!=float("inf") else "INF")