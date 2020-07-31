class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next




head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)


def print_ll(head):
	curr = head
	while curr != None:
		print(curr.val)
		curr = curr.next


print_ll(head)


# def reverseLinkedListRecursive(firstNode)
  
#   curr = firstNode
#   next = firstNode.next 

#   if next is None:
#     return curr
  
#   else:
#   	next = reverseLinkedList(firstNode.next)


#   current.next = prev
#   prev = current
#   current = nxt
#   nxt = current.next


# if last head:
# 	return last head

# otherwise:
# 	point to previous and remove last