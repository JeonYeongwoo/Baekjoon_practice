N = int(input())

search_list = list(map(int, input().split()))
dp_len_max = [1]
dp_last_value = [search_list[0]]

for i in range(1, N):
    cur_max = 1
    for j in range(len(dp_last_value)):
        if dp_last_value[j] < search_list[i] and cur_max < dp_len_max[j] + 1:
            cur_max = dp_len_max[j] +1
    dp_last_value.append(search_list[i])
    dp_len_max.append(cur_max)
    

print(max(dp_len_max))