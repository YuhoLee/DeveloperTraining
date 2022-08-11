testcase = int(input())
for test in range(testcase):
    # init
    t = int(input())
    arr = list(map(int, input().split()))
    dict = {i : 0 for i in range(101)}

    # start
    for num in arr:
        dict[num] += 1
    max_value = max(dict.values())
    max_num_list = []
    for k,v in dict.items():
        if v == max_value:
            max_num_list.append(k)
    print("#{} {}".format(t, max(max_num_list)))
