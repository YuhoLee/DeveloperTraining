def move(x,y,dir):
    if dir == 1:
        while arr[y][x-1] != 0:
            x -= 1
    elif dir == 2:
        while arr[y][x+1] != 0:
            x += 1
    y -= 1
    return x,y

while True:
    try:
        t = int(input())
        # 100 * 100 array
        # 양 옆 길 검사에 대한 처리를 편하게 하기 위해 양 옆에 길이 없는 0을 추가
        arr = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]
        # 거꾸로 따라가기
        res = 0
        x = arr[99].index(2)
        y = 99
        while y != 0:
            # dir 1: left, dir 2: right
            if arr[y][x-1] == 1:
                x,y = move(x,y,1)
            elif arr[y][x+1] == 1:
                x,y = move(x,y,2)
            else:
                y -= 1
        # 원래는 99인데 시작 시 검사 처리를 편하게 하기 위해 붙였던 0때문에 1증가

        res = x-1   # 위와 같은 이유로 진짜 인덱스 반환을 위해 1 감소
        print("#{} {}".format(t, res))
    except:
        break
