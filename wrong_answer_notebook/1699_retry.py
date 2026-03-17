# 지피티 솔루션 받은 후 추후 다시 풀이함

N = int(input())

# 제곱수 초기화 과정
pows = []
i=1
while (i**2 <= 100000):
    pows.append(i**2)
    i+= 1
    
dp_min_counts = [0, 1]
for i in range(2,N+1):
    min = i
    for j in pows:
        if i < j: 
            break
        if dp_min_counts[i-j] + 1 < min:
            min = dp_min_counts[i-j] + 1
    dp_min_counts.append(min)

print(dp_min_counts[N])