# https://www.acmicpc.net/problem/15666
# n과m (12)
# 중복 허용, 오름차순(비내림차순)
# 출력 오름차순, 수열 간 중복불가

import sys
input = sys.stdin.readline

n_len, length = map(int, input().split())
n_arr = list(map(int, input().split()))
n_arr.sort() #출력 오름차순

result = []

def permutation(start) :
    if len(result)==length :
        print(*result)
        return
    
    prev = -1
    for i in range(start, n_len) :
        n = n_arr[i]
        if prev!=n : # 수열 중복 방지
            result.append(n)
            permutation(i) # 오름차순. 중복허용이므로 다음에도 방금 사용한 숫자를 포함해서 넘겨줘야 함
            result.pop()
            prev = n

permutation(0)