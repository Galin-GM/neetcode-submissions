# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        current = head

        while current:
            length += 1
            current = current.next

        index = length - n

        if index == 0:
            return head.next

        current = head
        i = 0
        while current:
            if i + 1 == index:
                current.next = current.next.next
                break
            i += 1
            current = current.next

        return head