import math

N = int(input())
num_list = list(map(int, input().split()))

def sum_num():
    sum_return = 0
    for i in range(1, N):
        sum_return += abs(num_list[index[i]] - num_list[index[i-1]] )
    return sum_return
            

index = [i for i in range(N)]
answer = sum_num()

while (True):
    i = N-1
    while(i > 0 and index[i-1] >= index[i]):
        i -= 1
    if (i == 0):
        break
    else:
        j = N-1
        while (index[i-1] > index[j]):
            j -= 1
        index[i-1], index[j] = index[j], index[i-1]
        index[i::] = sorted(index[i::])
        # print (index)
        
        temp = sum_num()
        if (answer <=temp):
            answer = temp
            


print(answer)