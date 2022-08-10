sen = input()
stack = []
postfix = ''
for s in sen:
    if s not in ['+', '-', '*', '/', '(',')']:
        postfix += s
        continue
    if s in ['+', '-', '*', '/']:
        if len(stack) == 0:
            stack.append(s)
        else:
            if s == '*' or s == '/':
                if stack[-1] == '*' or stack[-1] == '/':
                    postfix += stack.pop(-1)
                stack.append(s)
            elif s == '+' or s == '-':
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

print(postfix)
