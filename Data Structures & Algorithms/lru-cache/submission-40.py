from dataclasses import dataclass, field

@dataclass 
class Node:
    key: int 
    value:int
    n: "Node | None" = field(default = None, repr = False, compare = False)
    p : "Node | None" = field(default = None, repr = False, compare = False)

class LRUCache:

    def _remove(self, node:Node):
        prev = node.p
        nex = node.n
        prev.n = nex
        nex.p = prev

    def _insert_first(self, node:Node):
        prev_first = self.head.n
        self.head.n = node
        node.n = prev_first
        node.p = self.head
        prev_first.p = node

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(-1, 0)
        self.tail = Node(-2, 0)
        self.head.n = self.tail
        self.tail.p = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._remove(node)
        self._insert_first(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        new_node = Node(key, value)

        if key in self.cache:
            old_node = self.cache[key]
            self._remove(old_node)
            del self.cache[key]
        self._insert_first(new_node)
        self.cache[key] = new_node

        if len(self.cache) > self.capacity:
            lru = self.tail.p
            self._remove(lru)
            del self.cache[lru.key]
        

