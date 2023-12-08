# https://www.acmicpc.net/problem/2252
# 순서 조건이 있는 요소들의 정렬 -> 위상정렬 -> 큐deque
# 위상정렬에서는 진입차수가 0인 노드를 찾아내야 하는데, 이걸 진입차수를 -1할 때 0이 되는지 체크하면 쉽게 할 수 있었다!
# 그래프를 2차원배열로 만들면 메모리초과 나서 딕셔너리로 바꿨더니 풀렸다~~
# 이건 예제는 통과하지만 채점은 메모리초과로 통과못한 2차원배열 코드.

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


#위상정렬에 사용할 큐, 방문 전인 노드 번호 배열, 큐에 시작점이 될 수 있는 노드 삽입
que = deque()
for i in range(1, v+1) :
    if inCnt[i]==0 : 
        que.append(i)

## 풀이 : 위상정렬
ans = []
while que : 
    cur = que.popleft()

    #큐에서 나온 순서(정답) 기록
    ans.append(cur)

    #이 노드에서 출발하는 간선 모두 삭제, 간선 도착점 노드의 진입차수도 수정
    for i in range(1, v+1):
        # 이 노드에서 출발하는 간선에 대해
        if graph[cur][i] :
            graph[cur][i] = False # 간선 삭제
            inCnt[i] -=1 # 진입차수 수정
            
            #방금 수정한 진입차수가 0이면? 큐에 넣음
            if inCnt[i]==0 :
                que.append(i)

print(*ans)