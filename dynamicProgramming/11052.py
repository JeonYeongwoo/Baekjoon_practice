N = int(input())

cost_pack = [0] + list(map(int, input().split()))

max_cost = [0 for _ in range(N+1)]
max_cost[1] = cost_pack[1]

# print (cost_pack)
for i in range(1, N+1):
    max = cost_pack[i] # 최소값 갱신할 변수
    
    for j in range(i//2, i):
        if (max_cost[j]):
            if (max_cost[j] + max_cost[i-j] > max): # 
                max = max_cost[j] + max_cost[i-j] 
        else:
            if (cost_pack[j] + max_cost[i-j] > max): # 
                max = max_cost[j] + max_cost[i-j] 
    
    
    max_cost[i] = max
    # print(max_cost) # 로그용
    
    
print(max_cost[N])

