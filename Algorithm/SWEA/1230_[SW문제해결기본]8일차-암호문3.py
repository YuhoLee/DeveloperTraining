# 테스트케이스 개수가 주어지지 않는 경우
# 1) sys.stdin으로 읽어오기
# 2) try~except 안에 while 루프문 선언하기
# sys를 사용하지 못하는 경우도 있기 때문에 2번 방법 추천
# 파이썬 버전 안맞아서 IDE에서 돌렸을 때랑 값이 다름,,,

def action(idx, cmd):
    global crypto
    if cmd == 'A':
        cnt = int(command[idx + 1])
        for s in command[idx+2:idx+cnt+2]:
            crypto.append(s)
        return cnt + 1
    else:
        pos = int(command[idx + 1])
        cnt = int(command[idx + 2])
        if cmd == 'I':
            crypto = crypto[:pos] + command[idx+3:idx+cnt+3] + crypto[pos:]
        elif cmd == 'D':
            for _ in range(cnt):
                crypto.pop(pos)
        return cnt+2

test = 0
while(True):
    try:
        n = int(input())
        crypto = list(input().split(' '))
        c = int(input())
        command = list(input().split())

        for i in range(len(command)):
            if command[i] in ['I', 'D', 'A']:
                action(i, command[i])

        s = ' '.join(crypto[:10])
        test += 1
        print("#{0} {1}".format(test, s))
    except:
        break

