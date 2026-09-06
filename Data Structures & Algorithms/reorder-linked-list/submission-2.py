# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        ## Find halfway point of the linked list
        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        ## Reverse second half of the linked list
        secondHalf = slow.next 
        prev = slow.next = None

        while secondHalf:
            temp = secondHalf.next
            secondHalf.next = prev
            prev = secondHalf
            secondHalf = temp
        
        ## Merge first and reversed second half together (second half will be same or shorter)
        ## prev is the head of the second half
        ## head is the head of the first half

        while prev:
            temp1, temp2 = head.next, prev.next
            head.next = prev
            prev.next = temp1
            head = temp1
            prev = temp2

