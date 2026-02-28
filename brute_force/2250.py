# right_node 개수랑 left_node 개수 저장하기
# 각 노드의 right 노드 개수는 right subtree 의 노드 개수 (left_node + right_node 개수)
# 이걸로 max_width_level 찾고
# max_width_level 노드의 레벨 출력 하면 되려나..?  

max_width_list = [1 for _ in range(10000)]

def max_update(level, count):
    if (level != 0):
        max_width_list[level] += count
class node:
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right
        self.left_count = 0
        self.right_count = 0
        
class binary_tree:
    def __init__(self, root = None):
        self.root = root
        self.level
        self.max_width
        
    def max_level(self):
        return self.level
    
    def max_width(self, level):
        return self.max_width
        

def insert(parent, node, left, right, count):
    if (parent.item == node):
        parent.left =  left
        parent.right = right
        
    if (parent.item >= node):
        parent.left_count += 1
        
        insert(parent.left, node, left, right, count)
    elif(parent.item < node):
        parent.right_count += 1
        insert(parent.right, node, left, right, count)
        
    
N = int(input())
tree = binary_tree()


for i in range(N):
    count = 0
    inp_arr = map(int, input().split())
    for j in range(3):
        if (inp_arr[j]):
            count += 1
    insert(tree.root, inp_arr[0], inp_arr[1], inp_arr[2], count)
    