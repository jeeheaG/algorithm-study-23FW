# https://www.acmicpc.net/problem/15655
# n과m (6)
# 중복불가, 오름차순, 사용할 숫자 주어짐
# 출력도 오름차순
# **nm(5)번까지 nums로 쓰던 변수명을 result로 변경함

n_len, length = map(int, input().split())
n_arr = list(map(int, input().split()))
n_arr.sort()

result = []

def permutation(start) :
    if len(result)==length :
        print(*result)
        return
    
    #시작위치 인덱스값이 필요해서 반복문 사용법만 살짝 바꾼 것. 해결 방식은 앞선 문제들과 똑같음!
    for i in range(start, n_len) :
        if n_arr[i] not in result :
            result.append(n_arr[i])
            permutation(i)
            result.pop()

permutation(0)