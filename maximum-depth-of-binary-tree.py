# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(self, root: TreeNode) -> int:

    current = [root]
    following = []
    count = 1
    
    for node in current:
        if current.left != None:
            following.append(current.left)
        if current.right !=None:
            following.append(current.right)  
        
    if following:
        count += 1
        current = following
        following = []
        
        do it again.
    
    else:
        return count

Root = TreeNode(3)
Root.left = TreeNode(9)
Root.left.left = null
Root.left.right = null
Root.right = TreeNode(20)
Root.right.left = TreeNode(15)
Root.right.right = TreeNode(7)

def print_binary_tree(head):
    curr_left = head
    curr_right = head

    while curr_left != None:
        print(curr.val)
        curr = curr.next

