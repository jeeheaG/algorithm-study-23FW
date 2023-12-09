# https://www.acmicpc.net/problem/15656
# n과m (7)
# 중복 허용, 숫자 주어짐
# 출력 오름차순

n_len, length = map(int, input().split())
n_arr = list(map(int, input().split()))
n_arr.sort()

result = []

def permutation() :
    if len(result)==length :
        print(*result)
        return
    
    for i in n_arr :
        result.append(i)
        permutation()
        result.pop()

permutation()