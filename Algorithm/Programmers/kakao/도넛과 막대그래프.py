def solution(edges):
    # in이 없는 놈이 정점임.
    se_graph = {}
    es_graph = {}
    for edge in edges:
        s, e = edge
        if s in se_graph:
            se_graph[s].append(e)
        else:
            se_graph[s] = [e]
            if s not in es_graph:
                es_graph[s] = []

        if e in es_graph:
            es_graph[e].append(s)
        else:
            es_graph[e] = [s]

    mp = -1
    for key in es_graph.keys():
        if len(es_graph[key]) == 0:
            if len(se_graph[key]) > 1:
                mp = key

    res = [mp, 0, 0, 0]
    for start in se_graph[mp]:
        node = start
        while True:
            if node in se_graph:
                nextCnt = len(se_graph[node])
                if nextCnt == 1:
                    if se_graph[node][0] == start:
                        # 도넛
                        res[1] += 1
                        break
                    else:
                        node = se_graph[node][0]
                else:
                    # 8자
                    res[3] += 1
                    break

            else:
                # 막대
                res[2] += 1
                break

    return res

solution([[2, 3], [4, 3], [1, 1], [2, 1]])
solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]])