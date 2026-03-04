import sys

# 탐색 리스트
N = int(input())
list_search = list(map(int, sys.stdin.readline().split()))
list_search.sort()

# 타겟 리스트
M = int(input())
list_target = list(map(int, sys.stdin.readline().split()))


# print(list_target)
# print(list_for_search)

for item in list_target:
    left = 0; right = len(list_search)-1;
    # print(left, right)
    mid = (left+right)// 2
    flag = 0
    
    while (left <= right):
        if (list_search[mid] == item):
            flag = 1 # 있다고 표시
            break
        
        if (item < list_search[mid] ) : # 타겟 아이템 밸류가 현 탐색값보다 작으면 -> 왼쪽으로
            right = mid - 1
        else: # 타겟 아이템 밸류가 현 탐색값보다 크면 탐색 범위를 오른쪽으로
            left = mid + 1
            
        mid = (left+right) // 2
        # print(mid)
        
    # print()
    if (flag == 1):
        print(1)
    else:
        print(0)
        
    