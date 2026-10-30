class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        
    def remove(self, node):
         #remove a node given key
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    def insert(self, node):
         #insert node at right
        prv, nxt = self.right.prev, self.right
        prv.next = nxt.prev = node
        node.prev, node.next = prv, nxt  

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(self.cache[lru.key])
            del self.cache[lru.key]
        
