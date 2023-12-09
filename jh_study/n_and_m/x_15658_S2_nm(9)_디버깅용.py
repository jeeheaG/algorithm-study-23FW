n_len, length = map(int, input().split())
n_arr = list(map(int, input().split()))
n_arr.sort()

visited = [False] * n_len
result = []
results = set() # 수열(result)들을 문자열로 변환하여 저장해둘 set

def permutation() :
    # 수열 하나 완성 시
    if len(result)==length :
        result_str = ' '.join(str(i) for i in result) #리스트를 공백으로 구분된 문자열로 변환해라
        results.add(result_str) # set이라 중복 알아서 처리
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

## 출력
print(*sorted(results), sep="\n")