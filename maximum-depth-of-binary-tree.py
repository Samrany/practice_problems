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
        
        # do it again.
    
    else:
        return count




def maxDepth2(root):
        nodes_list = [root]
        count = 0
        
        if root is None:
            return count

        while nodes_list:

            for x in range(len(nodes_list)):
                node = nodes_list.pop(0)

                if node.left:
                    nodes_list.append(node.left)

                if node.right:
                    nodes_list.append(node.right)

     
            count += 1
        return count


def maxDepth_recursive(root):
    if root is None:
        return 0
    else:
        return 1 + max(maxDepth1(root.left), maxDepth1(root.right))

Root = TreeNode(3)
Root.left = TreeNode(9)
Root.left.left = None
Root.left.right = None
Root.right = TreeNode(20)
Root.right.left = TreeNode(15)
Root.right.right = TreeNode(7)
Root.right.right.right = TreeNode(8)

print(maxDepth2(Root))

# def print_binary_tree(head):
#     curr_left = head
#     curr_right = head

#     while curr_left != None:
#         print(curr.val)
#         curr = curr.next

