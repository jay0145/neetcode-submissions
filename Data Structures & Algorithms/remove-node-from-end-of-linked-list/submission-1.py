# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        end = 0
        remove = ptr = head

        while ptr:
            end += 1
            ptr = ptr.next
        
        if end-n == 0:
            return head.next

        for i in range(end-n-1):
            #print(remove.val)
            remove = remove.next

        temp = remove.next.next
        remove.next = remove.next.next

        return head