from dataclasses import dataclass, field

@dataclass
class Node:
    key:int
    value:int
    nex: "Node | None" = field(default = None, repr = False, compare = False)
    prev: "Node | None" = field(default = None, repr = False, compare = False)

class LRUCache:
    def _remove(self, node:Node):
        prev = node.prev
        nex = node.nex
        prev.nex = nex
        nex.prev = prev
    
    def _insert_first(self, node:Node):
        nex = self.head.nex
        self.head.nex = node
        nex.prev = node
        node.prev = self.head
        node.nex = nex

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(-1,0)
        self.tail = Node(-2,0)

        self.head.nex = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            targetNode = self.cache[key]
            self._remove(targetNode)
            self._insert_first(targetNode)
            return targetNode.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        new_node = Node(key, value)

        if key in self.cache:
            old_node = self.cache[key]
            self._remove(old_node)
            del self.cache[old_node.key]
            
        self.cache[key] = new_node
        self._insert_first(new_node)
        
        if len(self.cache)>self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
