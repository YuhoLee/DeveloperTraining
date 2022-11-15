import heapq

t = int(input())
for test in range(1, t + 1):
    n, m, k, a, b = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    tp = list(map(int, input().split()))
    finish = False

    # aq: 접수 대기큐, bq: 정비 대기큐
    # wda: 접수 창구 리스트, wdb: 정비 창구 리스트
    # res: 고객이 지나간 창구를 담는 결과 리스트
    aq = []
    bq = []
    wda = [None] * n
    wdb = [None] * m
    res = [None] * k

    # 시간
    time = 0
    # 사람 번호
    pn = 0
    while not finish:

        # 시간이 되는대로 고객 입장
        while len(tp) > 0:
            if tp[0] == time:
                heapq.heappush(aq, pn)
                tp.pop(0)
                pn += 1
            else:
                break

        # 비어있는 접수창구가 있으면
        # 고객번호가 낮은 순으로 우선 입장
        # 빈 창구가 많을 때는 창구번호가 작은 곳부터 채움
        aql = len(aq)
        if aql != 0:
            for i in range(n):
                if aql != 0:
                    if wda[i] is None:
                        wda[i] = [heapq.heappop(aq), arr[i]]
                        aql -= 1
                else:
                    break

        # 접수 창구 처리 시간 1씩 흘러감
        # 만약 처리가 완료 되었다면 해당 창구에서 탈출하고 정비 대기큐로 이동
        buff = []
        for i in range(n):
            if wda[i] is not None:
                wda[i][1] -= 1
                if wda[i][1] == 0:
                    buff.append([wda[i][0],i])
                    wda[i] = None
        buff.sort(key=lambda x: x[1])
        for bf in buff:
            bq.append(bf)

        # 비어있는 정비 창구가 있으면
        # 먼저 온 순서부터 처리
        # 같이 온 경우는 접수 창구가 작은 순서로
        bql = len(bq)
        if bql != 0:
            for i in range(m):
                if bql != 0:
                    if wdb[i] is None:
                        bb = bq.pop(0)
                        bb.insert(1,brr[i])
                        wdb[i] = bb
                        bql -= 1
                else:
                    break

        # 정비 창구가 1씩 흘러감
        # 만약 처리가 완료되면 res 리스트에 고객의 번호에 맞는 인덱스에 접수창구와 정비창구의 번호를 넣어줌
        # 창구는 1부터 시작하는데 인덱스를 0부터 처리해, 1씩 더해줌
        for i in range(m):
            if wdb[i] is not None:
                wdb[i][1] -= 1
                if wdb[i][1] == 0:
                    res[wdb[i][0]] = [wdb[i][2] + 1, i + 1]
                    wdb[i] = None

        # 모든 고객에 대한 작업이 끝났다면
        # 반복문 종료를 위해 finish를 True로 바꿔줌
        flag = True
        for i in range(k):
            if res[i] is None:
                flag = False
                break
        if flag:
            finish = True

        # 시간 흘러감
        time += 1

    # 두 창구가 지갑을 잃어버린 고객과 같다면
    # 결과 값에 더해줌
    # 결과가 0 -> 두 창구가 모두 같은 고객이 없음 -> -1
    val = 0
    for i in range(k):
        if res[i] == [a, b]:
            val += (i + 1)
    if val == 0: val = -1
    print("#{} {}".format(test, val))