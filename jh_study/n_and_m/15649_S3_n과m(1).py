# https://www.acmicpc.net/problem/15649
# 중복불가, 모든 경우를 탐색해야 함
# n과 m (1)
# !!) list.append() 메서드는 반환값이 없음을 유의 ex) permutation(nums.append(i), cnt+1) 하면 함수에 리스트 전달 안됨

from sys import stdin
input = stdin.readline

n, length = map(int, input().split())

visited = [False] * (n+1)
nums = []

def permutation(cnt) :
    for i in range(1,n+1) :
        # 수열이 완성됐으면 return
        if cnt==length :
            print(*nums)
            return
        
        # 방문 전이면 방문 및 재귀
        if not visited[i] :
            visited[i] = True
            nums.append(i)
            permutation(cnt+1)
            nums.pop() #마지막값 제거
            visited[i] = False

permutation(0)