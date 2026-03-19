N = int(input())
inp = list(map(int, input().split()))

i = N-1
while (i > 0 and inp[i-1] < inp[i]): # 작은 
    i-= 1
    
if (i == 0):
    print(-1)
else:
    # [왼] pivot [오]
    # 오른쪽은 작은 것. -> pivot 보다 작은거 바로 감지되면? 그거랑 바꿈
    j = N-1
    while( inp[j] > inp[i-1]):
        j -= 1
        
    inp[j], inp[i-1] = inp[i-1], inp[j]
    inp[i:] = sorted(inp[i:], reverse=True)

    print(' '.join(map(str, inp)))