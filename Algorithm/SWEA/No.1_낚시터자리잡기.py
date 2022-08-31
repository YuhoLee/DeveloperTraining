from itertools import permutations

def DFS(gg, arr, stage):
    global min_count
    # 게이트 모두 탐색 시 최소값 비교
    if stage == 3:
        s = sum(arr)
        if min_count > s: min_count = s
        return
    # 게이트에 대한 위치와 사람 수
    pos, count = gate[gg[stage]]
    # 게이트 바로 앞에 위치해 있는 칸에 대한 수행
    if arr[pos] == 0:
        arr[pos] = 1
        count -= 1

    # 왼쪽, 오른쪽으로 거리 2가 차이날 때부터 시작
    pp = 2
    left, right = pos-1, pos+1
    flag = False
    # 카운트가 전부 다 닳을 때까지
    while count > 0:
        # 왼쪽과 오른쪽이 범위 내에 있고
        if 0 <= left < n and 0 <= right < n:
            # 마지막 한 사람이 들어 가야 하는데 왼쪽과 오른쪽이 모두 빈 경우
            # 두 시행 다 해주기 위해서 flag를 True로 만든 후 반복문 탈출
            if count == 1 and arr[left] == 0 and arr[right] == 0:
                flag = True
                break

        # 왼쪽이 범위 내에 있을 때
        if 0 <= left < n:
            # 비어 있다면
            if arr[left] == 0:
                # 그 곳에 인원 추가(게이트에서 떨어진 거리 추가)
                arr[left] = pp
                count -= 1

        # 사람이 모두 들어갔다면 반복문 탈출
        if count == 0: break

        # 오른쪽이 범위 내에 있을 때
        if 0 <= right < n:
            # 비어 있다면
            if arr[right] == 0:
                # 그 곳에 인원 추가(게이트에서 떨어진 거리 추가)
                arr[right] = pp
                count -= 1

        # 왼쪽, 오른쪽으로 한 칸씩 이동하고 거리 1 증가
        left -= 1
        right += 1
        pp += 1

    # 위에서 flag를 True로 주고 탈출한 경우
    if flag:
        # 왼쪽에 남은 한 사람을 채우고 다음 게이트 수행
        arr[left] = pp
        DFS(gg,arr[:],stage+1)
        # 오른쪽에 남은 한 사람을 채우고 다음 게이트 수행
        arr[left] = 0
        arr[right] = pp
        DFS(gg,arr[:],stage+1)
    # 사람이 모두 채워져서 탈출한 경우
    else:
        # 다음 게이트 수행
        DFS(gg,arr[:],stage+1)


t = int(input())
for test in range(1,t+1):
    # init
    n = int(input())
    gate = []
    for _ in range(3):
        p, c = map(int, input().split())
        gate.append((p-1,c))
    min_count = float('inf')
    # 게이트 방문 순서에 대한 경우의 수로 반복
    for gg in permutations(range(3),3):
        DFS(gg, [0]*n, 0)
    print("#{} {}".format(test, min_count))