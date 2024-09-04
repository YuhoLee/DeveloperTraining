acgt = ['A', 'C', 'G', 'T']

s, p = tuple(map(int, input().split()))
inputStr = input()
a, c, g, t = tuple(map(int, input().split()))
res = 0

acgtDict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for i in range(0, p - 1):
    if inputStr[i] in acgtDict: acgtDict[inputStr[i]] += 1

for i in range(p - 1, s):
    if inputStr[i] in acgt:
        acgtDict[inputStr[i]] += 1
        if acgtDict['A'] >= a and acgtDict['C'] >= c and acgtDict['G'] >= g and acgtDict['T'] >= t:
            res += 1

    if inputStr[i - p + 1] in acgtDict: acgtDict[inputStr[i - p + 1]] -= 1

print(res)
