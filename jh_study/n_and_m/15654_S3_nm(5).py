# https://www.acmicpc.net/problem/15654
# n과m (5)
# 사용할 숫자 데이터를 따로 줌(1~n 아님)
# 중복 불가
# 출력은 각 수열 간 오름차순으로. (수열 내에서는 상관x)

from sys import stdin
input = stdin.readline

n_len, length = map(int, input().split())
n_arr = list(map(int, input().split()))
n_arr.sort() #정렬 (오름차순 출력을 위해)

nums=[]

def permutation() :
    if len(nums)==length :
        print(*nums)
        return

    for i in n_arr :
        #이미 방문된(사용된) 숫자가 아닐 경우
        if i not in nums :
            nums.append(i)
            permutation()
            nums.pop()

permutation()