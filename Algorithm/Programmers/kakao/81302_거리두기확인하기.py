def searchAll(arr, i, j):
    length = len(arr)
    dir = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    dir2 = [[1, 1], [-1, 1], [1, -1], [-1, -1]]
    for k in range(4):
        y1, x1 = i + dir[k][1], j + dir[k][0]
        if 0 <= y1 < length and 0 <= x1 < length:
            p1 = arr[y1][x1]
            if p1 == 'P':
                return False
        y2, x2 = i + (dir[k][1] * 2), j + (dir[k][0] * 2)
        if 0 <= y2 < length and 0 <= x2 < length:
            p2 = arr[y2][x2]
            if p1 != 'X':
                if p2 == 'P':
                    return False

        y3, x3 = i + dir2[k][1], j + dir2[k][0]
        if 0 <= y3 < length and 0 <= x3 < length:
            p3 = arr[y3][x3]
            if p3 == 'P':
                if arr[i][x3] != 'X' or arr[y3][j] != 'X':
                    return False
    return True


def solution(places):
    answer = []
    for p in places:
        arr = []
        length = len(p)
        isGood = True
        for i in range(length):
            arr.append(list(p[i]))

        for i in range(length):
            for j in range(length):
                if arr[i][j] == 'P':
                    isGood = searchAll(arr, i, j)
                    if not isGood:
                        break
            if not isGood:
                break
        if isGood:
            answer.append(1)
        else:
            answer.append(0)

    return answer