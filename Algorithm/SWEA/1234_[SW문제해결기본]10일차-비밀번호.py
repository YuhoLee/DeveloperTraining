for test in range(1, 11):
    stack = []
    n, sen = tuple(input().split())
    n = int(n)
    stack.append(sen[0])
    for s in sen[1:]:
        if len(stack) != 0:
            if stack[-1] == s:
                stack.pop(-1)
            else: stack.append(s)
        else: stack.append(s)

    print("#{} {}".format(test, ''.join(stack)))
