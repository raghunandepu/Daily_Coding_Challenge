# https://www.hackerrank.com/contests/smart-interviews/challenges/si-implement-min-heap

# Partial (in progress)
class MinHeap:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def get(self, i):
        return self.items[i]
    
    # O based index
    def parent(self, i):
        return (i - 1) // 2
    
    def left(self, i):
        return (2*i + 1)
    
    def right(self, i):
        return (2*i + 1)
    
    def swap(self, i, j):
        self.items[i], self.items[j] = self.items[j], self.items[i]
            
    def insert(self, key):
        index = self.size()
        self.items.append(key)
        
        while index ! = 0:
            p = self.parent(index)
            if self.get(p) > self.get(index):
                self.swap(p, index)
            index = p
            
    min_Heap = MinHeap()
    