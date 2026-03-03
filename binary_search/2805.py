# 1654번 풀이 참고해서 풀이..
# 타겟은 total_height으로

import sys

N, M = map(int, input().split())

inp = list(map(int, sys.stdin.readline().split()))

inp.sort()

left = 1; right = inp[len(inp) -1]
mid = (left + right)// 2

total_tree_height = 0

while(left <= right):
    for h in inp:
        if (mid <= h):
            total_tree_height += h - mid
    
    if ( total_tree_height < M):
        right = mid -1
    else:
        left = mid +1
        
    mid = (left + right)// 2
    total_tree_height = 0
    
print(mid)