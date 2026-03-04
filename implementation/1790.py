N, K = map(int, input().split())

i = 1; j = 1
num_quantity = []
ans = -1

while ( i != 1000000000):
    num_quantity.append(j*9*i );
    i *= 10; j += 1;
    
# 1. k 찾는 매커니즘
# N_copy = N; 
# i_10_mul = 1; count = 1;
# k_check = 0 # 수 몇까지인지 파악

# while(True):
#     i_10_mul *= 10 # 10 ^ n 인지 파악
#     if ((N_copy // i_10_mul)  == 0):
#         break;
#     count += 1 # 몇 자리수 있는지 카운트

# # =========

# # 여기는 N_copy랑 count랑 k_check 사용
# if (count >= 2):
#     for i in range(count-2):
#         k_check += num_quantity[i]
#     k_check += count(N_copy - 10**(count-1)-1)

min_list = [9, 90, 900, 9000, 90000, 900000, 9000000,90000000,900000000]

result = 0
add = 1; N_copy = N; 
for k in range(len(min_list)):
    if (N_copy - min_list[k] >= 0):
        result += add * min_list[k]
    else:
        result += add * N_copy;
        break
    N_copy -= min_list[k]
    add += 1
    
# print("result:", result)

if (K > result):
    print(ans)
    exit(0)




# 2. 수 찾는 매커니즘
# print(num_quantity)
i = 0

while(True):
    
    if (K > num_quantity[i]):
        if (i == 0):
            K -= 1
        K -= (num_quantity[i])
        i += 1
        
    if (K <= num_quantity[i]):
        # print(K)
        temp = 0
        if (i == 0):
            # print(i)
            temp = str(K)
        else:
            # print(K//(i+1), K)
            temp = str((K // (i+1) )+ (10 **(i))) # 수
            # print(temp)
        temp2 = K % ((i+1)) 
        # if(temp2 == 0): temp2 = i 
        
        ans = temp[temp2]
        # print(temp)
        break
        
        
print(ans)
        
            
        
        