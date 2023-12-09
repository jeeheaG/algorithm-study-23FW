# https://www.acmicpc.net/problem/15651
# n과 m (3)
# 중복 허용!

n, length = map(int, input().split())

nums = []

def permutation() :
    if len(nums)==length :
        print(*nums)
        return

    #visited 체크 안함
    for i in range(1, n+1) :
        nums.append(i)
        permutation()
        nums.pop()

permutation()