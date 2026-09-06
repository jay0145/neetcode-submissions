# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        print("hello")
        while fast and fast.next:
            print(f"begin: {fast.val}, {slow.val}")
            print(f"{fast.next} and {fast.next.next}")
            fast = fast.next.next
            slow = slow.next


            if fast == slow:
                return True

        return False
            