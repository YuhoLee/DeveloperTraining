def factorial(k):
    n = 1
    for i in range(2,k+1):
        n *= i
    return n

def makePermutations(cnt, visited, pre):
    global total
    if cnt == l:
        total += 1
    for i in range(l):
        if not visited[i] and word[i] != pre:
            visited[i] = True
            makePermutations(cnt+1, visited, word[i])
            visited[i] = False

word = input()
l = len(word)
dict = {}
for s in word:
    if s in dict:
        dict[s] += 1
    else:
        dict[s] = 1
total = 0
makePermutations(0, [False]*l, '0')
for k in dict.values():
    total /= factorial(k)
print(int(total))