import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n=int(input())
tree=[0]*(1+n) #0-padding
tree={}
for _ in range(n):
    parent,leftchild,rightchild=input().split()
    tree[parent]=[leftchild,rightchild]

      
def preorder(currentnode):
    if currentnode=='.':
        return
    print(currentnode,end='')
    preorder(tree[currentnode][0])
    preorder(tree[currentnode][1])
def inorder(currentnode):
    if currentnode=='.':
        return
    inorder(tree[currentnode][0])
    print(currentnode,end='')
    inorder(tree[currentnode][1])
def postorder(currentnode):
    if currentnode=='.':
        return
    postorder(tree[currentnode][0])
    postorder(tree[currentnode][1])
    print(currentnode,end='')


preorder('A')
print()
inorder('A')
print()
postorder('A')   