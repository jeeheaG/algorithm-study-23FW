# https://www.acmicpc.net/problem/2252
# 순서 조건이 있는 요소들의 정렬 -> 위상정렬 -> 큐deque
# 위상정렬에서는 진입차수가 0인 노드를 찾아내야 하므로 이를 찾기쉽게 그래프를 딕셔너리가 아닌 2차원배열로 만들어봤다

from sys import stdin
from collections import deque #, defaultdict
input = stdin.readline

## 입력
v, e = map(int, input().split())

#간선, 노드별 진입차수 세두는 배열
graph = [[False] * (v+1) for _ in range(v+1)]
inCnt = [0] * (v+1)
for _ in range(e) :
    start, end = map(int, input().split())
    graph[start][end] = True
    inCnt[end] +=1

# print(*graph, sep="\n")
# print(inCnt)

#위상정렬에 사용할 큐, 방문 전인 노드 번호 배열, 큐에 시작점이 될 수 있는 노드 삽입
que = deque()
for i in range(1, v+1) :
    # print(node)
    if inCnt[i]==0 : 
        que.append(i)

# visited = [False] * (v+1)
# visited = [False, False, True, False] #함수 동작 테스트용

# 방문 전인 노드들 중 진입차수가 0인 노드만 큐에 넣는 함수
# def appendQue() :
#     for node in [i for i in range(1, v+1) if visited[i]==False] :
#         # print(node)
#         if inCnt[node]==0 : 
#             que.append(node)
# appendQue()


## 풀이 : 위상정렬
ans = []
while que : 
    cur = que.popleft()

    #큐에서 나온 순서(정답) 기록
    ans.append(cur)

    # #방문처리
    # visited[cur] = True

    #이 노드에서 출발하는 간선 모두 삭제, 간선 도착점 노드의 진입차수도 수정
    for i in range(1, v+1):
        # 이 노드에서 출발하는 간선에 대해
        if graph[cur][i] :
            graph[cur][i] = False # 간선 삭제
            inCnt[i] -=1 # 진입차수 수정
            
            #방금 수정한 진입차수가 0이면? 큐에 넣음
            if inCnt[i]==0 :
                que.append(i)
    
    # # 방문 전인 노드 중 진입차수가 0이 된 노드들을 큐에 넣음
    # appendQue()

print(ans)