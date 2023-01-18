class NodeList:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.dic = {}
        self.length = 0
        self.capacity = capacity
        self.dummy_head = NodeList()
        self.dummy_tail = NodeList()
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        
        node = self.dic[key]
        self.remove(node)
        
        node = NodeList(node.key, node.val)
        self.add(node)
        self.dic[key] = node
        
        return self.dic[key].val

    def put(self, key, value):
        node = NodeList(key, value)
        
        if key in self.dic:
            self.remove(self.dic[key])
            self.add(node)
            
        elif self.length < self.capacity:
            self.add(node)
            
        else:
            self.remove(self.dummy_head.next)
            self.add(node)
            
        self.dic[key] = node
            
    def add(self, node):
        curr_tail = self.dummy_tail.prev
        curr_tail.next = node
        node.prev = curr_tail
        
        node.next = self.dummy_tail
        self.dummy_tail.prev = node
        
        self.length += 1
            
    def remove(self, node):
        curr_prev = node.prev
        curr_next = node.next
        curr_prev.next = curr_next
        curr_next.prev = curr_prev

        del self.dic[node.key]
        self.length -= 1
        return node.val