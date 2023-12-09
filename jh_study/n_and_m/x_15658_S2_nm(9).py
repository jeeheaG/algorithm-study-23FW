# https://www.acmicpc.net/problem/15663
# n과m (9)
# 숫자 주어짐. 주어진 숫자들은 중복이 있을 수 있고, 주어진 중복 수 외에 중복사용 불가
# 출력에 중복이 있으면 안됨! 그리고 출력 오름차순

# 출력에 중복 막을 방법 : 1. 수열 모아놓고 중복 있는지 검사 2. ?
# 가 있을 것 같은데 일단 1번으로 해본다

n_len, length = map(int, input().split())
n_arr = list(map(int, input().split()))
n_arr.sort()

visited = [False] * n_len
result = []
# results = [] # 수열(result)들을 문자열로 변환하여 저장해둘 배열
results = set() # 수열(result)들을 문자열로 변환하여 저장해둘 set

def permutation() :
    # 수열 하나 완성 시
    if len(result)==length :
        result_str = ' '.join(str(i) for i in result) #리스트를 공백으로 구분된 문자열로 변환해라
        results.add(result_str) # set이라 중복 알아서 처리
        return

        # # 중복 수열 있는지 검사
        # result_str = ' '.join(str(i) for i in result) #리스트를 공백으로 구분된 문자열로 변환해라
        # if result_str in results :
        #     return # 중복이면 그냥 반환
        
        # # 중복 없으면 결과에 추가
        # results.append(result_str)
        # return
    
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