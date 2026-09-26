# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def display(head):
	        current = head
	        nodes = []          
	        while current:              
		        nodes.append(str(current.val))
		        current = current.next
	        print(' -> '.join(nodes))

        carry = 0
        dummy = ListNode()
        current = dummy
        
        while l1 or l2 or carry:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0

            x = (n1 + n2 + carry)
            carry = x // 10
            current.next = ListNode(val = x % 10)
            
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        display(dummy.next)
        return dummy.next