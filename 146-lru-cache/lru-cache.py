class Node:
    def __init__(self,key,val):
        self.key = key 
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.map = {} #store nodes themselves as the val
        self.capacity = capacity

        #doubly linekd lists 
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node):
        #skip 
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        #right before the right node
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev.next = node
        self.right.prev = node

    def get(self, key: int) -> int:
        if key in self.map:
            #grab existing node
            node = self.map[key]

            #remove the node and insert it again at the end    
            self.remove(node)     
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            #change val 
            node = self.map[key]
            node.val = value 
            self.remove(node)     
            self.insert(node)
        else:
            #new node + add 
            new_node = Node(key, value)
            self.map[key] = new_node

            self.insert(new_node)

        #LRU evict
        if len(self.map) > self.capacity:
            #acces the one before left
            remove_node = self.left.next

            self.remove(remove_node)
            del self.map[remove_node.key]





        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)