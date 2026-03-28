# 지피티 풀이 보고 나중에 재풀이함

from collections import deque

S = int(input())

# screen, clip 두개
cost = [[0 for _ in range (2001)] for _ in range(2001)]
visited = [[0 for _ in range (2001)] for _ in range(2001)]

cost[1][0] = 1; visited[1][0] = 1; 
cost[1][1] = 1; visited[1][1] = 1;

queue = deque()
queue.append([1,1])

# print(queue)
while(queue):
    screen, clip = map(int, queue.popleft())
    # print(screen, clip)
    cur_cost = cost[screen][clip]
    
    if (0 <= screen-1):
        if (visited[screen-1][clip] == 0):
            visited[screen-1][clip] = 1
            cost[screen-1][clip] = cur_cost + 1
            queue.append([screen-1, clip])
    if (screen + clip <= 2000):
        if (visited[screen+clip][clip] == 0):
            visited[screen+clip][clip] = 1
            cost[screen+clip][clip] = cur_cost + 1
            queue.append([screen+clip, clip])
    if (visited[screen][screen] == 0):
        visited[screen][screen] = 1
        cost[screen][screen] = cur_cost + 1
        queue.append([screen, screen])

print(min(cost[S][1:]))