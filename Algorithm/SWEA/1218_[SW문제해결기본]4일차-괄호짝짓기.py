for test in range(1, 11):
    n = int(input())
    arr = list(input())
    stack = []
    res = 1
    o_cnt, c_cnt = 0,0
    for i in range(n):
        if arr[i] in ['[', '{', '(']:
            o_cnt += 1
            stack.append(arr[i])
        else:
            if arr[i] in [']', '}', ')']:
                c_cnt += 1
                s = stack.pop(-1)
                if arr[i] == ']':
                    if s != '[':
                        res = 0
                        break
                if arr[i] == '}':
                    if s != '{':
                        res = 0
                        break
                if arr[i] == ')':
                    if s != '(':
                        res = 0
                        break
    if o_cnt != c_cnt: res = 0
    print("#{} {}".format(test, res))