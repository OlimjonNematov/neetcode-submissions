from dataclasses import dataclass, field

@dataclass 
class Node:
    key: int
    value:int
    p: "Node | None" = field(default = None, repr = False, compare = False)
    n: "Node | None" = field(default = None, repr = False, compare = False)

class LRUCache:
    
    def _remove(self, node: Node):
        prev = node.p
        nex = node.n
        prev.n = nex
        nex.p = prev
        node.p = None
        node.n = None

    def _insert_first(self, node: Node):
        old_first = self._head.n
        old_first.p = node
        self._head.n = node
        node.n = old_first
        node.p = self._head

    def __init__(self, capacity: int):
        self._cache = {}
        self._capacity = capacity
        self._head = Node(-1, 0)
        self._tail = Node(-2, 0)
        self._head.n = self._tail
        self._tail.p = self._head

    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1
        node = self._cache[key]
        self._remove(node)
        self._insert_first(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        new_node = Node(key, value)
        if key in self._cache:
            old_node = self._cache[key]
            self._remove(old_node)
            del self._cache[key]
        
        self._cache[key] = new_node
        self._insert_first(new_node)

        if len(self._cache) > self._capacity:
            lru = self._tail.p
            self._remove(lru)
            del self._cache[lru.key]
        
