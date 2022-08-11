test = int(input())
for t in range(1,test+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    # init
    num = {'0001101' : 0,'0011001' : 1,'0010011' : 2,'0111101' : 3,'0100011' : 4,
           '0110001' : 5,'0101111' : 6,'0111011' : 7,'0110111' : 8,'0001011' : 9}
    length = 7
    total = 0
    num_total = 0

    # 입력된 암호코드 해독
    # 한 줄씩 읽기
    for s in arr:
        # 역방향으로 '1'을 찾음
        # 0~9의 코드들이 다 1로 끝나는 암호코드를 가지고 있음 -> 이를 이용한 위치 파악
        # 이는 전체 코드문 중 암호문이 어디에 있는지 파악하기 위함
        idx = s.rfind('1')
        if idx != -1:
            # 암호코드 있는 부분만 추출
            buff = s[idx - 55:idx + 1]
            # 8칸으로 나눠서 추출
            for i in range(0, length * 8, length):
                # 해당 암호코드와 일치하는 숫자 저장
                num_buff = num[buff[i:i + length]]
                # 짝수면 3을 곱해서 총합에 더해줌
                if i % 2 == 0:
                    total += (num_buff * 3)
                # 홀수면 그냥 총합에 더해줌
                else:
                    total += num_buff
                # 숫자를 숫자합계에 더해줌
                num_total += num_buff
            # 10의 배수일 시 -> 검증
            if total % 10 == 0:
                break
            else:
                total, num_total = 0, 0

    print("#{} {}".format(t,num_total))
