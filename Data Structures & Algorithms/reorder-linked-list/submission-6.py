# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def display(head):
	        current = head
	        nodes = []          
	        while current:              
		        nodes.append(str(current.val))
		        current = current.next
	        print(' -> '.join(nodes))

        if not head.next:
            return

        # GET MIDDLE OF LIST
        slow = head
        fast = head
        previous = None
        while fast and fast.next:
            previous = slow
            slow = slow.next
            fast = fast.next.next

        # DISCONNECT TWO LISTS
        previous.next = None

        # REVERSE SECOND LIST
        previous = None
        current = slow
        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt

        # MERGE TWO LISTS
        first = head
        second = previous

        while first and second:
            next_first = first.next
            next_second = second.next

            first.next = second
            if next_first:
                second.next = next_first

            first = next_first
            second = next_second



