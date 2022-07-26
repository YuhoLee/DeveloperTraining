# 입력 횟수가 없어서 입력 끝날 시 종료할 수 있도록 함
for _ in range(10):
    # init
    test = int(input())
    a_max = 0
    # 회문 입력이 8*8이라 8번 input
    r_arr = [list(input()) for _ in range(100)]
    # row_arr의 전치행렬 (col단위 -> 세로 회문을 수월하게 찾기 위함)
    c_arr = list(zip(*r_arr))

    # 참조1
    # 글자 수마다 반복 횟수가 다름
    # 1글자 -> 8번, 2글자 -> 7번, 3글자 ->  6번 ....
    # stride = 1, row/col window size = n
    for n in range(100):
        complete = False
        # 가로 회문 계산
        for arr in r_arr:
            # 참조1
            for i in range(101 - n):
                # 1인 경우에는 모두 회문이므로 1씩 증가
                if n == 1:
                    a_max = 1
                # 1이 아닌 경우에는
                else:
                    # window 영역에 해당하는 문자열을 추출
                    buff = arr[i:i + n]
                    # 해당 영역의 문자열과 뒤집었을 때의 문자열이 같다면
                    if ''.join(buff) == ''.join(reversed(buff)):
                        # 회문이므로 맥스
                        a_max = n
                        complete = True
                        break
            if complete: break

        # 세로 회문 계산
        for arr in c_arr:
            # 참조1
            for i in range(101 - n):
                # 1인 경우에는 모두 회문이므로 1씩 증가
                if n == 1:
                    a_max = 1
                # 1이 아닌 경우에는
                else:
                    # window 영역에 해당하는 문자열을 추출
                    buff = arr[i:i + n]
                    # 해당 영역의 문자열과 뒤집었을 때의 문자열이 같다면
                    if ''.join(buff) == ''.join(reversed(buff)):
                        # 회문이므로 맥스
                        a_max = n
                        complete = True
                        break
            if complete: break

    print("#{0} {1}".format(test, a_max))
