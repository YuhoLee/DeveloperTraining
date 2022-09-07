import sys
sys.stdin = open("C:/Users/multicampus/Desktop/input.txt", "r")
test = int(input())
for t in range(1,test+1):
    n, m = map(int, input().split())
    arr = [sys.stdin.readline().strip() for _ in range(n)]
    # init
    code = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110',
            '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101',
            'E':'1110', 'F':'1111'}
    num_ratio = {'3211':'0', '2221':'1', '2122':'2', '1411':'3', '1132':'4', '1231':'5',
                 '1114':'6', '1312':'7', '1213':'8', '3112':'9',}

    length = 7
    total = 0
    res = 0

    arr = list(set(arr))
    l = len(arr)
    buff = []
    for i in range(l):
        arr[i] = arr[i].rstrip('0')
        end = len(arr[i])-1
        s = ''
        for j in range(end,-1,-1):
            s = code[arr[i][j]] + s
        s = s.rstrip('0')
        n1,n2,n3,n4 = 0,0,0,0
        sl = len(s)
        for i in range(sl-1,-1,-1):
            if s[i] == '1' and sum((n2,n3,n4)) == 0:
                n1 += 1
            elif s[i] == '0' and n1 != 0 and sum((n3,n4)) == 0:
                n2 += 1
            elif s[i] == '1' and n2 != 0 and n4 == 0:
                n3 += 1
            elif s[i] == '0' and n3 != 0:
                n4 += 1
                ratio = min((n1,n2,n3))
            if n4 != 0 and sum((n1,n2,n3,n4)) % (7*ratio) == 0:
                buff.append(str(n4//ratio) + str(n3//ratio) + str(n2//ratio) + str(n1//ratio))
                n1, n2, n3, n4 = 0, 0, 0, 0
    rl = len(buff)
    bb = []
    for i in range(rl//8):
        bb.append(''.join(buff[i*8:(i+1)*8]))
    bb = list(set(bb))
    for cb in bb:
        total = 0
        num_total = 0
        for i in range(7,-1,-1):
            pp = cb[i*4:(i+1)*4]
            # 짝수면 3을 곱해서 총합에 더해줌
            if i % 2 == 0:
                total += int(num_ratio[pp])
            # 홀수면 그냥 총합에 더해줌
            else:
                total += (int(num_ratio[pp]) * 3)
            num_total += int(num_ratio[pp])
        # 10의 배수일 시 -> 검증
        if total % 10 == 0:
            res += num_total
        total, num_total = 0, 0
    print("#{} {}".format(t, res))

