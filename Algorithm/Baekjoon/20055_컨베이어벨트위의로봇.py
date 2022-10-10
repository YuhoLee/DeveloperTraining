# 로봇 내리기
def take_robot():
    for i,rbt in enumerate(robot):
        if rbt == n-1:
            robot.pop(i)
            return


# 벨트 회전
def rotate():
    global up, down, robot
    upl = up[-1]
    downl = down[-1]
    up = [downl] + up[:n-1]
    down = [upl] + down[:n-1]
    for i in range(len(robot)):
        robot[i] += 1


# 로봇 움직이기
def move_robot():
    for i in range(len(robot)):
        flag = True
        for j in range(len(robot)):
            if robot[i] != robot[j]:
                if robot[i]+1 == robot[j]:
                    flag = False
                    break
        if flag and up[robot[i]+1] > 0:
            robot[i] += 1
            up[robot[i]] -= 1


# 첫 칸에 로봇 추가하기
def add_robot():
    if up[0] > 0:
        robot.append(0)
        up[0] -= 1


n,k = map(int, input().split())
arr = list(map(int, input().split()))
robot = []
up = arr[:n]
down = arr[n:]

stage = 0
while True:
    stage += 1
    rotate()
    take_robot()
    move_robot()
    take_robot()
    add_robot()
    # 내구도가 다 된 컴베이어 벨트 칸 개수 확인
    cnt = up.count(0) + down.count(0)
    if cnt >= k:
        break

print(stage)