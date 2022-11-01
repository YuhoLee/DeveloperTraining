# 벨만포드를 이용해 최단시간을 구하는 함수
def calc_shortest_time():
    # n라운드 진행
    for i in range(n):
        # 전체 엣지에 대해서 수행
        for j in range(m):
            # 출발도시, 도착도시, 걸리는 시간
            start,end,time = edge[j]
            # 현재 출발지점의 최단시간이 무한대가 아니고
            # 현재 지점의 시간에서 다음 지점으로 가는 시간을 더한 것이 기존 다음 지점까지 가는데 걸리는 시간보다 작을 때
            if dis[start] != float('inf') and dis[end] > dis[start] + time:
                # 더 짦기 때문에 더해준 값을 다음 지점까지 가는데 걸리는 시간으로 함
                dis[end] = dis[start] + time
                # 마지막 라운드에도 갱신이 된다면
                # 최단거리가 음의 무한대로 발산하는 cycle 존재 -> 최단거리 계산 불가능
                # cycle 발생하므로 True 반환
                if i == n-1:
                    return True
    # cycle이 없으므로 False 반환
    return False


# 시작 도시 1번
START_CITY = 1

# init
n,m = map(int, input().split())
dis = [float('inf')] * (n+1)
edge = [list(map(int, input().split())) for _ in range(m)]

# 시작 도시는 자기 자신이 기준이므로 0
dis[START_CITY] = 0
# 최단거리 계산 및 음의 cycle 존재 여부 확인
isCycle = calc_shortest_time()
# cycle 생성 시
if isCycle:
    print(-1)
else:
    for node in range(2,len(dis)):
        # 최단거리가 무한대가 아닐 경우
        # 1과 이어져있는 경로가 있을 경우
        if dis[node] != float('inf'):
            print(dis[node])
        else:
            print(-1)
