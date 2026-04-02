from collections import deque

import sys

N = int(sys.stdin.readline())
tree = []
for _ in range(N):
    tree.append(list(map(int, sys.stdin.readline().split())))
    
index = 0
dp = deque()
for i in range(1, N+1):
    dp.append([0 for _ in range(i)])
dp[0][0] = tree[0][0]; 
if (N > 1):
    dp[1][0] = tree[0][0]+ tree[1][0]; dp[1][1] = tree[0][0]+ tree[1][1]; 

for cur in range(2, N):
    dp[cur][0] = dp[cur-1][0] + tree[cur][0] 
    dp[cur][cur-1] = max(dp[cur-1][cur-1],dp[cur-1][cur-2]) + tree[cur][cur-1] 
    dp[cur][cur] = dp[cur-1][cur-1] + tree[cur][cur] 
    
    for j in range(1, cur-1):
        dp[cur][j] = max(dp[cur-1][j],dp[cur-1][j-1]) + tree[cur][j] 
        
        
# print(dp)
print(max(dp[N-1]))
    