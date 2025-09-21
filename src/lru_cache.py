
### `/src/lru_cache.py` (starter)
    
class _Node:
    __slots__ = ("key", "val", "prev", "next")
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        assert capacity > 0
        self.cap = capacity
        self.map = {}
        self.head = _Node("__H__", None)
        self.tail = _Node("__T__", None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        p, n = node.prev, node.next
        p.next = n
        n.prev = p

    def _insert_mru(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self._remove(node)
        self._insert_mru(node)
        return node.val

    def put(self, key, val):
        if key in self.map:
            node = self.map[key]
            node.val = val
            self._remove(node)
            self._insert_mru(node)
        else:
            if len(self.map) == self.cap:
                lru = self.tail.prev
                self._remove(lru)
                del self.map[lru.key]
            node = _Node(key, val)
            self.map[key] = node
            self._insert_mru(node)
