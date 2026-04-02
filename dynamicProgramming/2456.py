import sys

n = int(sys.stdin.readline())
wines = []


for _ in range (n):
    wines.append(int(sys.stdin.readline()))

dp = [[0 for _ in range(3)] for _ in range(n)]
dp[0][1] = wines[0]

for i in range(1, n):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = dp[i-1][0] + wines[i]
    if (dp[i-1][1]):
        dp[i][2] = dp[i-1][1] + wines[i]
    # print(dp[i-1])
    # print(dp[i])
    # print()    
    
print(max(dp[n-1]))