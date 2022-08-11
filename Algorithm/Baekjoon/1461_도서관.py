n,m = tuple(map(int, input().split(' ')))
arr = list(map(int,input().split(' '))) + [0]
arr.sort()
num_sum = 0
z = arr.index(0)
if z == 0:
    m_arr = []
    p_arr = arr[1:]
elif z == n-1:
    m_arr = arr[:n-1]
    p_arr = []
else:
    m_arr = arr[:z]
    p_arr = arr[z+1:]

try:
    if len(p_arr) == 0:
        for i in range(m):
            if i == 0: num_sum += abs(m_arr.pop(0))
            else: m_arr.pop(0)
    elif len(m_arr) == 0:
        for i in range(m):
            if i == 0: num_sum += p_arr.pop(-1)
            else: p_arr.pop(-1)
    else:
        if len(p_arr) == 0 or abs(m_arr[0]) > p_arr[-1]:
            for i in range(m):
                if i == 0: num_sum += abs(m_arr.pop(0))
                else: m_arr.pop(0)
        elif len(m_arr) == 0 or abs(m_arr[0]) <= p_arr[-1]:
            for i in range(m):
                if i == 0: num_sum += p_arr.pop(-1)
                else: p_arr.pop(-1)
except: pass

while len(m_arr) != 0:
    if len(m_arr) == 1:
        num_sum += abs(m_arr.pop(0)) * 2
        break
    else:
        num_sum += abs(m_arr.pop(0)) * 2
        for _ in range(m-1):
            if len(m_arr) != 0:
                m_arr.pop(0)
            else: break

while len(p_arr) != 0:
    if len(p_arr) == 1:
        num_sum += p_arr.pop(-1) * 2
        break
    else:
        num_sum += p_arr.pop(-1) * 2
        for _ in range(m-1):
            if len(p_arr) != 0:
                p_arr.pop(-1)
            else:
                break

print(num_sum)
