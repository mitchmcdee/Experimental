class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def snake_traverse(root):
    q = [root]
    direction = -1
    while len(q) != 0:
        print(' '.join(node.val for node in q[::direction]))
        q = [c for node in q for c in (node.left, node.right) if c]
        direction = -direction

def main():
    five = TreeNode('5', None, None)
    four = TreeNode('4', None, None)
    three = TreeNode('3', None, None)
    two = TreeNode('2', None, five)
    one = TreeNode('1', three, four)
    zero = TreeNode('0', one, two)
    r'''
        0
       / \
      1   2
     / \   \
    3   4   5
    '''
    snake_traverse(zero)

if __name__ == '__main__':
    main()
