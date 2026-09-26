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
        
        while l1 and l2:
            x = (l1.val + l2.val + carry)
            carry = x // 10
            current.next = ListNode(val = x % 10)
            current = current.next
            l1 = l1.next
            l2 = l2.next

        if carry and not l1 and not l2:
            current.next = ListNode(val = carry)
            return dummy.next

        if carry and l1:
            while carry and l1:
                x = l1.val + carry
                carry = x // 10
                current.next = ListNode(val = x % 10)
                current = current.next
                l1 = l1.next
            if carry:
                current.next = ListNode(val = carry)
            return dummy.next

        if carry and l2:
            while carry and l2:
                x = l2.val + carry
                carry = x // 10
                current.next = ListNode(val = x % 10)
                current = current.next
                l2 = l2.next
            if carry:
                current.next = ListNode(val = carry)
            return dummy.next

        if l1:
            current.next = l1
        elif l2:
            current.next = l2

        display(dummy.next)
        return dummy.next