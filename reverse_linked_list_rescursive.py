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


# class Solution(object):        
#     def reverseList(self, head):  # Iterative
#         prev, curr = None, head
#         while curr:
#             curr.next, prev, curr = prev, curr, curr.next
        
#         return prev
        

# public ListNode reverseList(ListNode head) {
#     if (head == null || head.next == null) return head;
#     ListNode p = reverseList(head.next);
#     head.next.next = head;
#     head.next = null;
#     return p;
# }


# reverseLinkedListStandard(head)


def reverseLinkedListRecursive(head):

	if head == None or head.next == None:
		return head

	else:
		nxt  = reverseLinkedListRecursive(head.next)
		head.next.next = head;
		head.next = None;
		return nxt

# 	while current.next is not None:
# 		current.next  = reverseLinkedListRecursive(current.next)

# 	else:
# 		return current 


reverse = reverseLinkedListRecursive(head)
print_ll(reverse)

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