t = int(input())
for test in range(1,t+1):
    # init
    n, l = map(int, input().split())
    r_arr = [list(map(int, input().split())) for _ in range(n)]
    c_arr = list(map(list, zip(*r_arr)))
    count = 0

    # 가로, 세로에 대해
    for arr in [r_arr,c_arr]:
        # 경사로 유무를 나타내는 2차원 배열
        slope = [[False] * n for _ in range(n)]
        # 한 줄씩 검사
        for p,line in enumerate(arr):
            i = 0
            while True:
                # 한 줄을 무사히 탐색했다면 카운트 1 증가하고 탈출
                if i >= n:
                    count += 1
                    break

                elif i < n-1:
                    can = True
                    # 현재와 다음 칸의 차이가 1보다 클 시 카운트X, 탈출
                    if abs(line[i+1]-line[i]) > 1:
                        break
                    # 현재 칸보다 다음 칸이 큰 경우
                    if line[i] < line[i+1]:
                        # 첫 칸부터 경사를 놓아야 하는데 경사로 길이가 한 칸이 아닐 시 -> 탈출
                        # 딱히 예외 처리 방법이 생각이 안나서,,
                        if i == 0 and l > 1:
                            break
                        # 경사로가 놓일 부분에 대해서 검사
                        for j in range(i-l+1,i+1):
                            if 0 <= j < n:
                                # 칸 높이가 같지 않거나 이미 경사로가 놓인 곳이라면
                                # 카운트 없이 탈출
                                if line[j] != line[i] or slope[p][j]:
                                    #     print("line[i]: {}, line[j]: {}, slope[j]: {}".format(line[i],line[j],slope[i][j]))
                                    can = False
                                    break
                            else:
                                can = False
                                break
                        if not can:
                            break
                        # 경사로가 놓인 부분에 대해 True로 표시함
                        for k in range(i-l+1,i+1):
                            if 0 <= k < n:
                                slope[p][k] = True
                    # 현재 칸보다 다음 칸이 작은 경우
                    elif line[i] > line[i+1]:
                        # 마지막 칸수들이 경사로 길이보다 작은 경우 -> 탈출
                        # 이거도 딱히 예외 처리 방법이 생각이 안나서,,,
                        if i+l >= n:
                            break
                        # 경사로가 놓일 부분에 대해 검사
                        for j in range(i+1,i+l+1):
                            if 0 <= j < n:
                                # 놓일 칸들의 높이가 모두 같은지 확인하기 위해
                                # 놓일 칸의 처음을 기준으로 하여 비교
                                # 하나라도 같지 않다면 카운트 없이 탈출
                                if j == i+1: st = line[j]
                                else:
                                    if line[j] != st:
                                        can = False
                                        break
                            else:
                                can = False
                                break
                        if not can:
                            break
                        # 경사로가 놓인 부분에 대해 True로 표시함
                        for k in range(i+1,i+l+1):
                            if 0 <= k < n:
                                slope[p][k] = True
                        # 놓인 부분의 마지막 칸으로 이동
                        i = i+l-1
                i += 1
    print("#{} {}".format(test,count))