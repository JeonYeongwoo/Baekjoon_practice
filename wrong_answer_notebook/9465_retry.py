# 지피티 풀이 보고 2틀 뒤 다시 구현..

from collections import deque
import sys

T = int(input())

answers = []
for _ in range(T):
    n = int(sys.stdin.readline())
    stickers = [];
    for _ in range(2):
        stickers.append(list(map(int, sys.stdin.readline().split())))
    
    if (n == 1):
        
        print(max([stickers[0][0], stickers[1][0]]))
        continue
    if (n == 2):
        print(max ([stickers [0][0] + stickers [1][1]
                    , stickers[1][0] + stickers[0][1]]))
        continue
    
    dp = [[0 for _ in range(n)] for _ in range (2)] 
    dp[0][0] = stickers[0][0]; dp[1][0] = stickers[1][0]; 
    dp[1][1] = stickers[0][0] + stickers[1][1]; dp[0][1] = stickers[1][0] + stickers[0][1];
    
    for i in range(2, n):
        for j in range(2):
            if (j == 0):
                dp[0][i] = max(dp[0][i-2], dp[0][i-3], dp[1][i-1], dp[1][i-2]) + stickers[j][i]
            else: 
                dp[1][i] = max(dp[1][i-2], dp[1][i-3], dp[0][i-1], dp[0][i-2]) + stickers[j][i]
    
    # print(dp)
    answers.append(max(dp[0][n-1],dp[0][n-2],dp[1][n-1],dp[1][n-2]))
    
    
for ans in answers:
    print(ans)