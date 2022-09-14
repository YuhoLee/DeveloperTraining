t = int(input())
for test in range(1,t+1):
    n = int(input())
    word = input()
    dict_list = []
    l = len(word)
    for i in range(1,l+1):
        for j in range(0,l-i+1):
            dict_list.append(word[j:j+i])
    dict_list = sorted(list(set(dict_list)))
    if len(dict_list) > n-1:
        print("#{} {}".format(test, dict_list[n-1]))
    else:
        print("#{} none".format(test))