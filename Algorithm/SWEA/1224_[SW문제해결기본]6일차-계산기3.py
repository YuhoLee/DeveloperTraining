def calc(words):
    buff = []
    for i in range(len(words)):
        if words[i] in ['+', '*']:
            a = buff.pop()
            b = buff.pop()
            if words[i] == '+':
                buff.append(str(int(a)+int(b)))
            elif words[i] == '*':
                buff.append(str(int(a)*int(b)))
        else: buff.append(words[i])
    return buff

for t in range(1,11):
    n = int(input())
    sen = input()
    stack = []
    postfix = ''
    for s in sen:
        if s not in ['+','*','(',')']:
            postfix += s
            continue
        if s in ['+','*']:
            if len(stack) == 0:
                stack.append(s)
            else:
                if s == '*':
                    if stack[-1] == '*':
                        postfix += stack.pop(-1)
                    stack.append(s)
                elif s == '+':
                    while len(stack) != 0 and stack[-1] != '(':
                        postfix += stack.pop(-1)
                    stack.append(s)
        elif s == '(': stack.append(s)
        elif s == ')':
            while True:
                if len(stack) != 0 and stack[-1] != '(':
                    postfix += stack.pop(-1)
                else:
                    if stack[-1] == '(':
                        stack.pop(-1)
                    break

    while len(stack) != 0:
        postfix += stack.pop(-1)

    print("#{} {}".format(t, calc(postfix)[0]))