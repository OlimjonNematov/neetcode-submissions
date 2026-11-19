from dataclasses import dataclass, field

@dataclass 
class Node:
    key:int
    value:int
    n: "Node | None" = field(default = None, repr = False, compare = False)
    p: "Node | None" = field(default = None, repr = False, compare = False)

class LRUCache:

    def _remove(self, node: Node):
        prev = node.p
        nex = node.n
        prev.n = nex
        nex.p = prev
    
    def _insert(self, node:Node):
        nex = self.head.n
        nex.p = node
        self.head.n = node
        node.n = nex
        node.p = self.head

    def __init__(self, capacity: int):
        self.cache_map = {}
        self.capacity = capacity
        self.head = Node(-1, 0)
        self.tail = Node(-2, 0)
        self.head.n = self.tail
        self.tail.p = self.head

    def get(self, key: int) -> int:
        if key in self.cache_map:
            node = self.cache_map[key]
            self._remove(node)
            self._insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.cache_map:
            old = self.cache_map[key]
            self._remove(old)
            self._insert(node)
        else:
            self.cache_map[key] = node
            self._insert(node)

        self.cache_map[key]=node
        if len(self.cache_map) > self.capacity:
            lru = self.tail.p
            print(lru)
            self._remove(lru)
            del self.cache_map[lru.key]


        
