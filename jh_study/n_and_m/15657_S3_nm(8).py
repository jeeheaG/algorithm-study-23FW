# https://www.acmicpc.net/problem/15657
# n과m (8)
# 중복 허용, 오름차순(비내림차순)
# 출력도 오름차순

n_len, length = map(int, input().split())
n_arr = list(map(int, input().split()))
n_arr.sort()

result = []

def permutation(start) :
    if len(result)==length :
        print(*result)
        return
    
    for i in range(start, n_len) :
        result.append(n_arr[i])
        permutation(i)
        result.pop()

permutation(0)