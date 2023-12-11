# https://www.acmicpc.net/problem/15665
# n과m (10)
# 중복 허용, 숫자 주어짐
# 출력 오름차순, 수열 중복없이

import sys
input = sys.stdin.readline

n_len, length = map(int, input().split())
n_arr = list(map(int, input().split()))
n_arr.sort() # 출력 오름차순을 위함

result = []

def permutation() :
    if len(result)==length :
        print(*result)
        return

    prev = -1
    for n in n_arr :
        if prev!=n : # 수열의 중복 제거 
            result.append(n)
            permutation()
            result.pop()
            prev = n

permutation()