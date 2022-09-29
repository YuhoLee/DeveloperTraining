from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for n in course:
        buff = []
        for menu in orders:
            case = combinations(menu, n)
            for m in case:
                buff.append(''.join(sorted(m)))
        candidates = Counter(buff).most_common()
        print(candidates)
        answer += [res for res, c in candidates if c == candidates[0][1] and c > 1]
    answer = sorted(answer)

    return answer