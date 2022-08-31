from itertools import permutations

def hunt(order):
    global min_distance
    huntList = []
    # 헌터 초기 위치
    hunter = (0,0)
    dis = 0
    # 처음 방문이 고객일 때 -> 종료
    # 잡은 몬스터 없이 고객을 방문하는 것은 무의미한 시행
    if order[0] < 0: return
    # 받은 경우의 수에 대해
    for ord in order:
        # 고객일 때
        if ord < 0:
            # 고객이 원하는 몬스터가 사냥한 몬스터 리스트에 없으면
            # 무의미한 시행이므로 종료
            if -ord not in huntList: return
            # 원하는 몬스터가 있다면
            else:
                # 유클리드 거리를 구하여 전체 거리에 더해줌
                oy, ox = customer[-ord]
                dis += (abs(oy - hunter[0]) + abs(ox - hunter[1]))
                # 사냥꾼이 해당 고객 위치로 이동
                hunter = customer[-ord]
        # 몬스터일 때
        elif ord > 0:
            # 사냥한 몬스터 리스트에 추가
            huntList.append(ord)
            # 유클리드 거리를 구하여 전체 거리에 더해줌
            my, mx = monster[ord]
            dis += (abs(my-hunter[0]) + abs(mx-hunter[1]))
            # 사냥꾼이 해당 몬스터 위치로 이동
            hunter = monster[ord]

    # 무사히 전부 이동 완료했다면 거리 최소값 비교
    if min_distance > dis: min_distance = dis


t = int(input())
for test in range(1,t+1):
    # init
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    mc = []
    monster, customer = [0]*5,[0]*5
    # 몬스터 및 고객의 종류를 mc배열에 넣어주고
    # 몬스터와 고객의 위치를 리스트에 저장
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                mc.append(arr[i][j])
                if arr[i][j] > 0: monster[arr[i][j]] = (i,j)
                else: customer[-arr[i][j]] = (i,j)
    min_distance = float('inf')
    # 모든 방문 순서의 경우의 수에 대해 탐색 시작
    case = list(permutations(mc,len(mc)))
    for c in case:
        hunt(c)
    print("#{} {}".format(test, min_distance))