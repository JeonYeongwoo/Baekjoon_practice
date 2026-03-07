N = int(input())

cost_pack = [0] + list(map(int, input().split()))

min_cost = [0 for _ in range(N+1)]
min_cost[1] = cost_pack[1]

# print (cost_pack)
for i in range(1, N+1):
    min = cost_pack[i] # 최소값 갱신할 변수
    
    for j in range(i//2, i):
        if (min_cost[j]):
            if (min_cost[j] + min_cost[i-j] < min): # 
                min = min_cost[j] + min_cost[i-j] 
        else:
            if (cost_pack[j] + min_cost[i-j] < min): # 
                min = min_cost[j] + min_cost[i-j] 
    
    
    min_cost[i] = min
    # print(min_cost) # 로그용
    
    
print(min_cost[N])

