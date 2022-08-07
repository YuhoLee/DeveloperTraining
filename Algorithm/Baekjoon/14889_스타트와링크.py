from itertools import combinations
import math

# 해당 팀의 총 능력치 반환
def calc_sum(case):
    # 1) combinations 없이 구현
    # sum = 0
    # l = len(case)
    # for i in range(l):
    #     for j in range(i+1,l):
    #         sum += (arr[case[i]][case[j]] + arr[case[j]][case[i]])

    # 2) combinations 사용하여 구현
    # 같은 팀 내에서 두 선수 씩 짝지어지는 경우의 수를 구하여 능력치 계산
    for i,j in list(combinations(case,2)):
        sum += (arr[i][j] + arr[j][i])
    return sum

# init
n = int(input())
arr = [list(map(int, input().split(' '))) for _ in range(n)]
min_res = math.inf
caseList = list(combinations(range(n),n//2))

# 두 팀의 차이가 '최소'가 되는 결과값 계산
# 서로 상대팀이 되는 경우를 매칭하여 계산
# ex) list(combinations([1,2,3,4], 2)) -> [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
# 일 때 'idx 0과 -1, idx 1과 -2, idx 2와 -3 ' 이렇게 매칭되게 됨.
# 이를 공식화 해보면 인덱스 매칭 시 i와 (i+1)*(-1)로 접근하여 매칭하게 됨.
# 반복 한번 당 두 팀이 매칭되기에 전체 경우의 수 1/2 만큼 반복
for i in range(len(caseList)//2):
    # 두 팀 능력치에 대한 차이 반환
    res = abs(calc_sum(caseList[i]) - calc_sum(caseList[(i+1)*(-1)]))
    # 차이 최소값 반환
    if min_res > res:
        min_res = res
print(min_res)