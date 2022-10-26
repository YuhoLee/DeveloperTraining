# init
n,m = map(int, input().split())
# 인접 행렬 형태로 받음
arr = [[1]*(n+1)] + [[1]+[0]*n for _ in range(n)]
for _ in range(m):
    s,t = map(int, input().split())
    arr[s][t]= 1

# 플로이드 워셜
# path는 중간 지점 노드
for path in range(1,n+1):
    # i는 시작 노드
    for i in range(1,n+1):
        if path != i:
            # j는 끝 노드
            for j in range(1,n+1):
                if path != j and i != j:
                    # path라는 중간지점을 거쳐서 i에서 j를 알 수 있다면
                    # i에서 j를 알 수 있기에 1을 대입
                    if arr[i][path] == 1 and arr[path][j] == 1:
                        arr[i][j] = 1
res = 0
# 두 노드 p1과 p2
for p1 in range(1,n+1):
    linked = 0
    for p2 in range(1,n+1):
        if p1 != p2:
            # arr[p1][p2] -> 1이면 p1이 p2보다 작음을 알 수 있는 상태
            # arr[p2][p1] -> 1이면 p2가 p1보다 작음을 알 수 있는 상태
            # 둘 다 1일 수는 없음. -> 둘 다 0이거나 하나만 1
            linked += (arr[p1][p2] + arr[p2][p1])
    # 자신을 제외하고 모든 노드와 연결되었을 시
    if linked == n-1:
        # 연결될 수 있는 노드에 대한 카운트 증가
        res += 1
print(res)