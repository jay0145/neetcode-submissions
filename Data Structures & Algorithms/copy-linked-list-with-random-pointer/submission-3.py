"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        newHead = prev = curr = None
        tempH = head
        nodes = {}
        while tempH:
            curr = Node(tempH.val)
            if not newHead:
                newHead = curr
            nodes[tempH] = curr
            if prev:
                prev.next = curr

            prev = curr
            tempH = tempH.next

        if curr:
            curr.next = None
        else:
            return None

        #reset both to beginnning 

        #print(head.next.random)
        
        curr = newHead
        """
        while curr:
            print(curr.val)
            curr = curr.next
        """
        tempH = head
        while curr:
            if tempH.random in nodes:
                curr.random = nodes[tempH.random]
            else:
                curr.random = None
            #print(f"{curr.val} {tempH.val}")
            curr = curr.next
            tempH = tempH.next
            
        
        return newHead
        


