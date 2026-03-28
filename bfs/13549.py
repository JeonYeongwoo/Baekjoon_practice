from collections import deque

N, K = map(int, input().split())

cost = [0 for _ in range(200001)]
visited = [0 for _ in range(200001)]
queue = deque()
prev_info_list = deque()
queue.append(N); cost[N] = 0; prev_info_list.append([N, 0])
# ================
# print(stack)
while(queue):
    current = queue.popleft()
    prev_info = prev_info_list.popleft()
    # print(current)
    if (visited[current] == 1):
        continue
    visited[current] = 1 
    if (prev_info[1] == 1):
        cost[current] = cost[prev_info[0]] + 1
    else:
        cost[current] = cost[prev_info[0]]
    # print(prev_info)
    if (2 * current <= 200000 and current != 0):
        if (visited[2*current] == 0):
            queue.append(2*current)
            prev_info_list.append([current, 0])
    
    if (current -1 >= 0):
        if (visited[current-1] == 0):
            queue.append(current-1)
            prev_info_list.append([current, 1])
            
    if (current +1 <= 200000):
        if (visited[current+1] == 0):
            queue.append(current+1)
            prev_info_list.append([current, 1])
        
            
print (cost[K])
        
        
    