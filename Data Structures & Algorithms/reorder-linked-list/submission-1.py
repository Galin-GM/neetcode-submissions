# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def get_last(head):
            previous = None
            current = head
            
            while current.next:
                nxt = current.next
                previous = current
                current = nxt
            
            if previous:
                previous.next = None
            
            return current


        current = head

        while current:
            c = get_last(current)
            if c == current:
                break
            c.next = current.next
            current.next = c
            current = current.next.next

