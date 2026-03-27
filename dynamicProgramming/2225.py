N, K = map(int, input().split())

# 중복조합 문제로 치부 가능
# 0을 중간에 끼우면 다 다른 것이기 때문에
# N개의 1을 K개로 나눈다고 생각하면 됨.
# nHr = n+r-1Cr / n == N 이고 r == K 이므로
# N+K-1CN 의 값을 구하면 됨..

# 최대는 N = 200, K = 200 일 때이니깐
# 대강 400까지 구해버리자
dp = [[0 for _ in range(401)] for _ in range(401)]

# 파스칼 삼각형 구현 ~ 400까지
dp[0][0] = 1
dp[1][0] = 1; dp[1][1] = 1
 
for i in range(2, 401): # 몇 수
    dp[i][0] = 1
    
    for j in range(1, i+1):
        dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % 1000000000 # 1000000000 으로 나눈 수이므로
    dp[i][i] = 1
    # if (i < N+K-1):
    #     print(dp[i][:i+1])

# print(dp[N+K-1][:N+K-1])
print(dp[N+K-1][N])

