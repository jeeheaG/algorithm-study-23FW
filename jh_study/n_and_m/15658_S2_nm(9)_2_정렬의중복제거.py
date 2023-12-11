# https://www.acmicpc.net/problem/15663
# n과m (9)
# 숫자 주어짐. 주어진 숫자들은 중복이 있을 수 있고, 주어진 중복 수 외에 중복사용 불가
# 출력에 중복이 있으면 안됨! 그리고 출력 오름차순
# !!) 정렬되어있을 경우 중복체크 팁 : 정렬되어있으므로 이전 값과 다르다면 중복이 아님! 이전 값과의 비교만으로 중복 확인이 가능함. 이게 dict사용 방법보다 메모리, 시간 효율 모두 좋음
# !!) 순서를 유지하고 중복을 제거하는 방법 : 딕셔너리 dict.fromkeys() 메서드를 활용. for문 사용할 수도 있지만 시간초과남


n_len, length = map(int, input().split())
n_arr = list(map(int, input().split()))
n_arr.sort()

visited = [False] * n_len
result = []
results_str = [] # 수열(result)들을 문자열로 변환하여 저장

def permutation() :
    # 수열 하나 완성 시
    if len(result)==length :
        print(*result)
        return
    
    # 오름차순이므로 중복 체크 시 이전것과 다르다면 중복이 아님
    prev = -1 # 이전숫자를 기억해둘 변수
    for i in range(n_len) :
        # 아직 사용 안한 숫자이고, 이전 숫자와 다른 수라면
        if not visited[i] and prev!=n_arr[i]:
            # 사용
            visited[i] = True
            result.append(n_arr[i])
            permutation()
            # 사용 끝난 후
            result.pop()
            visited[i] = False
            prev = n_arr[i] #직전 사용 숫자로 기억

permutation()