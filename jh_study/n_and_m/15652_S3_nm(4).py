# https://www.acmicpc.net/problem/15652
# n과m (4)
# 중복 허용, 오름차순(비내림차순=오름차순 또는 중복수라는 뜻)
# 오름차순인 n과m(2) 와 중복허용인 n과m(3) 을 합치면 쉽게 풀림

n, length = map(int, input().split())

nums = []

def permutation(start) :
    if len(nums)==length :
        print(*nums)
        return
    
    for i in range(start, n+1) :
        nums.append(i)
        permutation(i)
        nums.pop()

permutation(1)