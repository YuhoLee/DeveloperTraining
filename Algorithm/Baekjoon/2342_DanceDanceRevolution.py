# 어떤 발이 p에서 목표 지점 까지 갈 때
def move(before,after):
    # 같은 곳일 경우
    if before == after: return 1
    # 이전 발의 위치가 0인 경우
    elif before == 0: return 2
    # 반대 방향의 위치인 경우
    elif abs(after-before)%2 == 0: return 4
    # 인접한 지점의 경우
    else: return 3


# init
arr = list(map(int, input().split()))
arr.pop(-1)
s = len(arr)
if s == 0:
    print(0)
    exit()

# 움직일 지점 * 오른발 * 왼발
dp = [[[float('inf')]*5 for _ in range(5)] for _ in range(s+1)]
dp[-1][0][0] = 0

# for i,d in enumerate(dp):
#     for s in d:
#         print(s)
#     print("n = {}".format(i))
#     print('----------------')

# 움직여야 될 지점 만큼
for n in range(s):
    # 왼발이 고정된 상태에서 오른발의 움직임에 따른 dp계산
    for j in range(5):
        for p in range(5):
            dp[n][arr[n]][j] = min(dp[n][arr[n]][j], dp[n-1][p][j] + move(p,arr[n]))
    # 오른발이 고정된 상태에서 왼발의 움직임에 따른 dp계산
    for i in range(5):
        for p in range(5):
            dp[n][i][arr[n]] = min(dp[n][i][arr[n]], dp[n-1][i][p] + move(p,arr[n]))

# print("결과")
# for i,d in enumerate(dp):
#     for s in d:
#         print(s)
#     print("n = {}".format(i))
#     print('----------------')

mm = min([min(m) for m in dp[s-1]])
print(mm)