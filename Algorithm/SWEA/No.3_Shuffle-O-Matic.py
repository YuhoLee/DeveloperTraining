# 카드패 섞기
# 왼쪽, 오른쪽으로 나눔
def shuffle(left, right, x):
    global n, p
    res = [0] * n
    pp = 0

    # x값에 따라 왼쪽, 오른쪽 리스트에 담긴 요소들이 이동하는 칸 수가 다름
    # left 리스트, right 리스트
    for i in range(p):
        dx = x-pp
        if dx > p: dx = p
        elif dx < 0: dx = 0
        res[p-i-1+dx] = left[p-i-1]
        res[i+p-dx] = right[i]
        pp += 1

    return res


def DFS(arr, count):
    global min_shuffle, n, p
    # 셔플을 5번 초과로 했다면 종료
    if count > 5:
        return
    # 현재 카드패가 정렬되어있다면
    if arr == sorted_arr or arr == reverse_sorted_arr:
        # 섞은 횟수가 최소인지 확인 후 종료
        if min_shuffle > count:
            min_shuffle = count
            return

    # x=1 ~ x=5 로 카드패 섞어보기
    for x in range(1, n):
        buff = shuffle(arr[:p], arr[p:], x)
        DFS(buff[:], count + 1)


t = int(input())
for test in range(1, t + 1):
    # init
    n = int(input())
    p = n // 2
    arr = list(map(int, input().split()))
    min_shuffle = float('inf')
    # 정방향, 역방향으로 정렬된 카드 비교를 위해 저장해둠
    sorted_arr = sorted(arr)
    reverse_sorted_arr = sorted(arr, reverse=True)
    DFS(arr[:], 0)
    # 그대로 무한대면 -> 정렬 불가 -> -1 출력
    if min_shuffle == float('inf'): print("#{} {}".format(test,-1))
    else: print("#{} {}".format(test,min_shuffle))