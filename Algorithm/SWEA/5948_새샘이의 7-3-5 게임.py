# 브루트포스의 경우 파이썬에서 지원하는 combination을 사용하면 편리하지만 코테에서는 사용 불가능 할 것으로 예상
def game(v, c):
    if c >= 3:
        total = 0
        for i,check in enumerate(v):
            if check:
                total += arr[i]
        maxList.append(total)
        return

    visited = v[:]
    for i,n in enumerate(arr):
        # 기존 visited를 사용하면 안되기에 반복할 때마다 복사해주어야 함 ==> 시간복잡도 증가
        # 따라서 재귀함수가 종료되면 visited를 다시 바꿔주어 다음 재귀함수 수행에 영향을 미치지 않도록 하였음.
        if not visited[i]:
            visited[i] = True
            game(visited, c+1)
            visited[i] = False

testcase = int(input())
for test in range(testcase):
    arr = list(map(int, input().split(' ')))
    maxList = []
    game([False] * 7, 0)
    maxList = list(sorted(set(maxList)))
    print("#{0} {1}".format(test+1, maxList[-5]))
