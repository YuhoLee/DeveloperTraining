import heapq

t = int(input())
for test in range(1,t+1):
    n,m,k,a,b = map(int, input().split())
    arr = list(map(int, input().split()))
    brr = list(map(int, input().split()))
    person = list(map(int, input().split()))
    finish = False

    aq = []
    bq = []
    wda = [None] * n
    wdb = [None] * m



