# https://www.acmicpc.net/problem/15650
# n과 m (2)
# 중복불가, 오름차순만

n, length = map(int, input().split()) #입력이 이게 다라서 그냥 input()씀

visited = [False] * (n+1)
visited[0] = True
nums = []

def permutation(start, cnt) :
    for i in range(start, n+1) :
        if cnt==length :
            print(*nums)
            return
    
        if not visited[i] :
            visited[i] = True
            nums.append(i)
            permutation(i, cnt+1)
            nums.pop()
            visited[i] = False

permutation(1, 0)