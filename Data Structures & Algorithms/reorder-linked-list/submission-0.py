# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        curr = head
        dq = collections.deque()
        ordered = []

        while curr:
            dq.append(curr)
            curr = curr.next
        
        left = True
        while dq:
            if left:
                ordered.append(dq.popleft())
                left = False
            else:
                ordered.append(dq.pop())
                left = True
        
        for i in range(len(ordered)-1):
            ordered[i].next = ordered[i+1]
        
        ordered[-1].next = None