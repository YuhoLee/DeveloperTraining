# dfs
def dfs(mm,c):
    global curr, flag
    # 모든 상담에 대해 처리를 완료했다면
    # flag True 후 리턴
    if c == n:
        flag = True
        return

    # 남아있는 상담에 대해
    for i,(s,e) in enumerate(task):
        # 현재 시간이 s와 e 사이에 있고 가능한 케이스가 아직 나오지 않았다면
        if s <= mm <= e and not flag:
            # 해당 상담을 빼줌
            v = task.pop(i)
            # 다음 상담 탐색
            dfs(mm+1,c+1)
            # 다른 상담에 대한 탐색을 위해 복구
            task.insert(i,v)
        else: break


t = int(input())
for test in range(1,t+1):
    n,m = map(int, input().split())
    # 상담 테스크 입력
    task = [list(map(int, input().split())) for _ in range(n)]
    # 먼저 상담 가능한 순으로 정렬
    task.sort(key=lambda x: x[0])
    # 결과값
    res = -1
    # 연속 상담 가능 여부 flag
    flag = False

    # 1부터 m까지 순차적으로 검사
    # 가능한 대로 바로 종료
    for i in range(1,m+1):
        curr = i
        dfs(i,0)
        if flag:
            res = curr
            break
    print("#{} {}".format(test,res))