# 지피티한테 로직 받음
# 구현만 함 (1일 뒤에 다시 복기해서 안보고)
import sys

N = int(input())

graph = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
parents = [-1 for _ in range(N+1)]
stack = []

for _ in range(N-1):
    i1, i2 = map(int, sys.stdin.readline().split())
    graph[i1].append(i2)
    graph[i2].append(i1)

visited[1] = 1
stack.append(1)
while(stack):
    cur = stack.pop()
    
    for u in graph[cur]:
        if (visited[u] == 0 ):
            visited[u] = 1
            stack.append(u)
            parents[u] = cur
            
for i in range(2, N+1):
    print(parents[i])
            
        