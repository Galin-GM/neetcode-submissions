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

        # def get_last(head):
        #     previous = None
        #     current = head
            
        #     while current.next:
        #         nxt = current.next
        #         previous = current
        #         current = nxt
            
        #     if previous:
        #         previous.next = None
            
        #     return current


        # current = head

        # while current:
        #     c = get_last(current)
        #     if c == current:
        #         break
        #     c.next = current.next
        #     current.next = c
        #     current = current.next.next

        if not head.next:
            return

        slow = head
        fast = head
        previous = None
        while fast and fast.next:
            previous = slow
            slow = slow.next
            fast = fast.next.next

        previous.next = None

        previous = None
        current = slow

        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt

        display(head)
        display(previous)

        current = head
        while current:
            print(previous.val)
            tmp1 = previous.next
            tmp2 = current.next
            previous.next = current.next
            current.next = previous
            if tmp2:
                current = tmp2
            else:
                break
            previous = tmp1
            
        previous.next = tmp1


