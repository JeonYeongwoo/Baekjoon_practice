import sys
# 각각 N, M
N, M = map(int, input().split()) 

tetrominos = [ [ [1,1,1,1] ],
              [[1,1],[1,1]],             
              [[1,0], [1,0],[1,1]],              
              [[1,0],[1,1],[0,1]],
              [[1,1,1],[0,1,0]]]

def rotate(item): 
    temp =[]
    for _ in range(len(item[0])):
        temp.append([0 for _ in range(len(item))])
        
    # print(temp)
    for j in range(len(item)):
        for i in range(len(item[0])): # col 갯수만큼 반복
            # row 갯수만큼 반
            temp[i][len(item) - 1 - j] = item[j][i]
    
    for tet in tetrominos:
        if (temp == tet):
            return
    tetrominos.append(temp)

def reverse(item): # 대칭시키는걸 생각 안했음..
    temp =[]
    for _ in range(len(item)):
        temp.append([0 for _ in range(len(item[0]))])
        
    for i in range(len (item)):
        for j in range(len(item[0])):
            j_index = len(item[0])-1 - j
            temp[i][j] = item[i][j_index]
            
    for tet in tetrominos:
        if (temp == tet):
            return
    tetrominos.append(temp)


# print(tetrominos)  
i = 1
for tet in tetrominos:
    to_append = []
    temp_row_to_append = []
    rotate(tet)   
    reverse(tet)   
    if(i == 50):
        break      
    i += 1     

# print(len(tetrominos))
# i = 1
# for tet in tetrominos:
#     to_append = []
#     temp_row_to_append = []
    
#     if(i == 50):
#         break      
#     i += 1   

# for i in range(len(tetrominos)):
#     to_append = []
#     temp_row_to_append = []
#     reverse(tetrominos[i])   

# print(len(tetrominos))

# for tet in tetrominos:
#     for row_tet in tet:
#         print(row_tet)
#     print()      

mat = []
for _ in range(N):
    mat.append(list(map(int, sys.stdin.readline().split())))
    
max = 0
for i in range(N): # row - row
    for j in range(M): # col - col
        for tet in tetrominos:
            sum = 0
            if (i + (len(tet)) > N):
                continue
            if (j + (len(tet[0])) > M):
                continue
            for k in range(len(tet)): # row
                for m in range(len(tet[0])): # cols
                    if (tet[k][m] == 1):
                        sum += mat[i+k][j+m]

            if (max < sum):
                max = sum
    #     print(i)
    # print(tet, max)
print(max) 
    