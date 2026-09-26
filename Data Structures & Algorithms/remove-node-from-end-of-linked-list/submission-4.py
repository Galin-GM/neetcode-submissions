# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # length = 0
        # current = head

        # while current:
        #     length += 1
        #     current = current.next

        # index = length - n

        # if length == 1:
        #     head.next = None
        #     return

        # previous = None
        # current = head
        # i = 0

        # while current:
        #     if i == index:
        #         if previous:
        #             previous.next = current.next
        #         else:
        #             head = head.next
        #     i += 1
        #     nxt = current.next
        #     previous = current
        #     current = nxt

        i = 0
        left = None
        right = head
        prev = None

        while right:
            if i == n:
                left = head
            i += 1
            right = right.next
            if left:
                tmp = left.next
                prev = left
                left = tmp
        
        if left:
            prev.next = left.next
        else:
            head = head.next


        return head