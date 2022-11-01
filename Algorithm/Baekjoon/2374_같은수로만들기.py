# 최댓값을 기준으로 왼쪽 오른쪽으로 나누어 살펴보는 함수
def division(arr_list):
    global res
    s = len(arr_list)

    # 리스트 길이가 1일 때 -> 나눌게 없으므로 해당 리스트 원소 반환
    if s == 1: return arr_list[0]
    # 리스트 길이가 0일 때 -> 나눠질 리스트가 없으므로 None 반환
    if s == 0: return None

    # 리스트 내 최댓값 구하기
    max_num = max(arr_list)
    # 최댓값이 존재하는 인덱스 반환
    idx = arr_list.index(max_num)

    # 최댓값을 기준으로 왼쪽 / 오른쪽으로 나눔
    # 결과값은 나눈 리스트의 최댓값을 반환함
    left = division(arr_list[:idx])
    right = division(arr_list[idx+1:])

    # 나온 left와 right가 None이 아니라면
    # 위에서 구한 최댓값에서 나누어진 left, right의 최댓값들을 각각 빼서 결과에 더해줌
    if left is not None:
        res += max_num - left
    if right is not None:
        res += max_num - right

    # 최댓값 반환
    return max_num


n = int(input())
arr = [int(input()) for _ in range(n)]
res = 0
division(arr)
print(res)

