class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.LRU = ListNode(0,0)
        self.mostUsed = ListNode(0,0)
        self.LRU.next = self.mostUsed
        self.mostUsed.prev = self.LRU

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def append(self, node):
        self.mostUsed.prev.next = node
        node.prev = self.mostUsed.prev
        node.next = self.mostUsed
        self.mostUsed.prev = node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        self.remove(self.cache[key])
        self.append(self.cache[key])

        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
        else:
            self.cache[key] = ListNode(key, value)
        
        #print(self.cache[key].val)
        self.append(self.cache[key])


        if len(self.cache) > self.capacity:
            self.cache.pop(self.LRU.next.key)
            self.remove(self.LRU.next)
        
