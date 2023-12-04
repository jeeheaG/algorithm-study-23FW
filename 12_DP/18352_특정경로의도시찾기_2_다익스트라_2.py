# 최단거리 ->bfs->큐deque / 또는 ->다익->우선순위큐heapq, 그래프
from sys import stdin
import heapq
input = stdin.readline #입력방식대체

## 입력
n, m, k, x = map(int, input().split())

#그래프 노드번호 인덱싱 쉽게 +1
graph = [[] * (n+1) for _ in range(n+1)]

#경로 입력받기 : heapq에 넣기 편하게 튜플로 경로 저장(2차원배열이나 딕셔너리로 안하고)
for _ in range(m) :
    start, end = map(int, input().split())
    graph[start].append((1, end)) #가중치가 모두 동일하므로 1로 통일

# print(*graph, sep="\n")

# 최단거리값 모음
dist_arr = [float("INF")] * (n+1)

# 우선순위큐와 시작점 설정
que = []
heapq.heappush(que, (0, x)) # 시작노드는 현재노드이므로 거리 = 0
dist_arr[x] = 0 # 시작노드 최단거리값 갱신해주고 시작함

## 다익스트라
while que :
    # 제일 가까운 노드 pop
    dist, cur = heapq.heappop(que)

    # 이미 방문하여 최단거리가 구해진 노드인지 확인
    if dist > dist_arr[cur] :
        continue # 인접노드 탐색 안함

    # 인접노드 탐색
    for ndist, nxt in graph[cur] :
        # 이 길로 인접노드에 갔을 때 비용
        cost = dist + ndist
        
        # 새로운 최단거리라면 갱신 후 인접노드를 큐에 추가
        if cost < dist_arr[nxt] :
            dist_arr[nxt] = cost
            heapq.heappush(que, (cost, nxt))

## 출력
# print(*dist_arr)
isExist = False
for i, node in enumerate(dist_arr[1:]) :
    if node == k :
        print(i+1)
        isExist = True

if not isExist :
    print(-1)