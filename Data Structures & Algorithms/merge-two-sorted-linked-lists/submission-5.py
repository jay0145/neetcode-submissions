# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1, l2 = list1, list2

        result = head = ListNode()

        while l1 or l2:
           #print(l1.val, l2.val)
            if (l1 and l2 and l1.val < l2.val) or not l2:
                result.next = l1
                l1 = l1.next
            elif (l1 and l2 and l1.val >= l2.val) or not l1:
                result.next = l2
                l2 = l2.next
            

            result = result.next
            
        return head.next
            

            

