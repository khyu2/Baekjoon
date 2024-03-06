import sys
input = lambda: sys.stdin.readline().rstrip()

class Node:
  def __init__(self, value, left, right):
    self.value = value
    self.left = left
    self.right = right

def preorder(node):
  if node.value != '.': print(node.value, end='')
  if node.left != '.': preorder(tree[node.left])
  if node.right != '.': preorder(tree[node.right])

def inorder(node):
  if node.left != '.': inorder(tree[node.left])
  if node.value != '.': print(node.value, end='')
  if node.right != '.': inorder(tree[node.right])

def postorder(node):
  if node.left != '.': postorder(tree[node.left])
  if node.right != '.': postorder(tree[node.right])
  if node.value != '.': print(node.value, end='')

tree = {}

n = int(input())
for _ in range(n):
  root, l, r = input().split()
  tree[root] = Node(root, l, r)

preorder(tree['A'])
print()

inorder(tree['A'])
print()

postorder(tree['A'])
