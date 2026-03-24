# 다시 코드 공부할 필요 있음. -> 지피티를 이용해서 버그 2개 잡음. (B 및 P 명령어 수행 시 : 다음 노드의 이전 노드를 재연결시키지 않음.)

import sys
from collections import deque

class Node:
    def __init__(self, item, next, prev):
        self.item = item
        self.next = next
        self.prev = prev
    
start = Node(None, None, None)
current = start
# === 정상 작동

inp = sys.stdin.readline()

for item in inp:
    current.next = Node(item, None, current)
    current = current.next 
current.item = ''
current = current.prev
    
# === 정상

N = int(input())

for _ in range(N):
    inp = sys.stdin.readline().split()

    if (inp[0] == 'L'):
        if(current.item != None): # 맨 처음
            current = current.prev
    elif (inp[0] == 'D'):
        if((current.next).item != ''):
            current = current.next
    elif (inp[0] == 'B'): # 얘가 시작 노드를 수정 못하게 해야 함.
        if (current != start):
            temp = current.prev
            temp.next = current.next
            
            # 지피티로 잡은 버그..
            (current.next).prev = temp
            
            current = current.prev
    elif (inp[0] == 'P'):
        temp = Node(inp[1], current.next, current)
        
        # 지피티로 잡은 버그.. 다음 노드의 이전 노드를 수정하지 않음..
        (current.next).prev = temp
        
        current.next = temp
        current = current.next
    
start = start.next # 시작 다음으로 옮김 (시작 아이템은 None)
if (start.item == ''):
    print()
else:
    while(start.item != ''):
        sys.stdout.write(start.item +'')
        start = start.next