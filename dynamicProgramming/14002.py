# 11053 + 백트랙킹

N = int(input())

search_list = list(map(int, input().split()))
dp_len_max = [1]
dp_last_value = [search_list[0]]

precedessors = [0]


for i in range(1, N):
    cur_max = 1
    precedessor = i
    for j in range(len(dp_last_value)):
        if dp_last_value[j] < search_list[i] and cur_max < dp_len_max[j] + 1:
            cur_max = dp_len_max[j] +1
            precedessor = j
    dp_last_value.append(search_list[i])
    dp_len_max.append(cur_max)
    precedessors.append(precedessor)

max_index = 0
max_len = 0
for i in range(len(dp_len_max)):
    if (max_len < dp_len_max[i]):
        max_len = dp_len_max[i]
        max_index = i
        
print(max_len)
current_index = max_index
ans_list = []
for i in range(max_len):
    ans_list.append(dp_last_value[current_index])
    current_index  = precedessors[current_index]

ans_list.sort()
for item in ans_list:
    print(item, end = " ")
# print(precedessors)
# print(dp_len_max)
    