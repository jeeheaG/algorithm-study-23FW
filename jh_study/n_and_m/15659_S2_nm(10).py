# https://www.acmicpc.net/problem/15664
# n과m (10)
# 주어진 숫자만 사용(중복있음). 오름차순
# 출력 오름차순, 수열 간 중복없이

import sys
input = sys.stdin.readline

n_len, length = map(int, input().split())
n_arr = list(map(int, input().split()))
n_arr.sort()

result = []

def permutation(start) :
    if len(result)==length :
        print(*result)
        return
    
    prev = -1
    for i in range(start, n_len) :
        if prev!=n_arr[i] : # 수열 중복 제거
            result.append(n_arr[i])
            permutation(i+1) #방금 사용한 숫자의 다음 숫자부터만 사용 -> 오름차순 보장
            result.pop()
            prev = n_arr[i]

permutation(0)