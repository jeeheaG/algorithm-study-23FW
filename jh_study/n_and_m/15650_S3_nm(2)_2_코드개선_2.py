# https://www.acmicpc.net/problem/15650
# n과 m (2) 코드개선 버전. 개선점 2가지
# 중복불가, 오름차순만

n, length = map(int, input().split())

nums = []

def permutation(start, cnt) :
    # 1. cnt값은 함수가 새로 호출될 때에만 바뀌므로 함수 시작점에서만 검사하면 됨. 반복문 안에 들어가있을 필요가 없음
    if cnt==length :
        print(*nums)
        return
    
    for i in range(start, n+1) :
        # 2-2. 사용된 앞쪽 부분은 잘라서 전달하므로 중복 체크 필요 없음
        nums.append(i)
        permutation(i+1, cnt+1)
        nums.pop()

permutation(1, 0)