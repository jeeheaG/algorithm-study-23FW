# https://www.acmicpc.net/problem/15663
# n과m (9)
# 숫자 주어짐. 주어진 숫자들은 중복이 있을 수 있고, 주어진 중복 수 외에 중복사용 불가
# 출력에 중복이 있으면 안됨! 그리고 출력 오름차순
# !!) 순서를 유지하고 중복을 제거하는 방법 : dict.fromkeys() 메서드를 활용. for문 사용할 수도 있지만 시간초과남

n_len, length = map(int, input().split())
n_arr = list(map(int, input().split()))
n_arr.sort()

visited = [False] * n_len
result = []
results_str = [] # 수열(result)들을 문자열로 변환하여 저장

def permutation() :
    # 수열 하나 완성 시
    if len(result)==length :
        result_str = ' '.join(str(i) for i in result) #리스트를 공백으로 구분된 문자열로 변환해라
        results_str.append(result_str)
        return
    
    for i in range(n_len) :
        # 아직 사용 안한 숫자라면
        if not visited[i] :
            # 사용
            visited[i] = True
            result.append(n_arr[i])
            permutation()
            # 사용 끝난 후
            result.pop()
            visited[i] = False

permutation()

# 중복제거 (순서 유지됨)
sorted_results_str = list(dict.fromkeys(results_str))

## 출력
print(*sorted_results_str, sep="\n")