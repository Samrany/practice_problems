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

def reverseLinkedListStandard(head):
        curr = head         

        if curr:
            
            prev = None
            nxt = curr.next

            while nxt != None:
                curr.next = prev
                prev = curr
                curr = nxt
                nxt = curr.next

            curr.next = prev
        
        return curr


reverseLinkedListStandard(head)


# def reverseLinkedListRecursive(current):

# 	while current.next is not None:
# 		current.next  = reverseLinkedListRecursive(current.next)

# 	else:
# 		return current 


# print_ll(reverseLinkedListRecursive(head))

	# while curr.next != None:
	# 	curr.next = recursion(cur)

	# else:
	# 	return curr


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