dir = [[0,0],[0,-1],[1,0],[0,1],[-1,0]]


def distance(x,y,px,py):
    return abs(px-x)+abs(py-y)


def calc_performance(a_pos,b_pos):
    ax,ay = a_pos
    bx,by = b_pos
    a_possible = []
    b_possible = []
    a_charge, b_charge = 0, 0
    for i,(px,py,c,p) in enumerate(bc_info):
        if distance(ax,ay,px,py) <= c:
            a_possible.append(i)
        if distance(bx,by,px,py) <= c:
            b_possible.append(i)

    la,lb = len(a_possible),len(b_possible)
    if la and lb:
        if la == 1 and lb == 1:
            if a_possible[0] == b_possible[0]:
                return bc_info[a_possible[0]][3]
            else:
                return bc_info[a_possible[0]][3] + bc_info[b_possible[0]][3]
        elif la == 1:
            a_charge = bc_info[a_possible[0]][3]
            b_possible = [x for x in b_possible if x not in a_possible]
            for idx in b_possible:
                cc = bc_info[idx][3]
                if b_charge < cc: b_charge = cc
            return a_charge + b_charge
        elif lb == 1:
            b_charge = bc_info[b_possible[0]][3]
            a_possible = [x for x in a_possible if x not in b_possible]
            for idx in a_possible:
                cc = bc_info[idx][3]
                if a_charge < cc: a_charge = cc
            return a_charge + b_charge
        else:
            res_max = 0
            for i in range(la):
                for j in range(lb):
                    if a_possible[i] == b_possible[j]: continue
                    rr = bc_info[a_possible[i]][3] + bc_info[b_possible[j]][3]
                    if res_max < rr: res_max = rr
            return res_max
    elif la:
        for idx in a_possible:
            cc = bc_info[idx][3]
            if a_charge < cc: a_charge = cc
        return a_charge
    elif lb:
        for idx in b_possible:
            cc = bc_info[idx][3]
            if b_charge < cc: b_charge = cc
        return b_charge
    else: return 0


t = int(input())
for test in range(1,t+1):
    m,c = map(int, input().split())
    a_deeds = list(map(int, input().split()))
    b_deeds = list(map(int, input().split()))
    bc_info = [list(map(int, input().split())) for _ in range(c)]
    a_pos,b_pos = [1,1],[10,10]
    res = calc_performance(a_pos,b_pos)
    for i in range(m):
        adx,ady = dir[a_deeds[i]]
        bdx,bdy = dir[b_deeds[i]]
        a_pos[0] += adx
        a_pos[1] += ady
        b_pos[0] += bdx
        b_pos[1] += bdy
        sub = calc_performance(a_pos,b_pos)
        res += sub
    print("#{} {}".format(test,res))