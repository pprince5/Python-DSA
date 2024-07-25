#    Main Author(s): Prince Prince
#    Main Reviewer(s): Kexian Guo, Kiran Dhillon
class HashTable:
    def __init__(self, cap=32):
        self.cap = cap
        self.size = 0
        self.table = [None] * cap

    def _hash(self, key):
        return hash(key) % self.cap

    def _resize(self):
        old_table = self.table
        self.cap *= 2
        self.table = [None] * self.cap
        self.size = 0
        
        for entry in old_table:
            if entry is not None:
                key, value = entry
                self.insert(key, value)
    
    def insert(self, key, value):
        index = self._hash(key)
        start_index = index
        
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return False  # Key already exists
            index = (index + 1) % self.cap
            if index == start_index:
                return False  # Table is full
        
        self.table[index] = (key, value)
        self.size += 1
        
        if self.size / self.cap > 0.7:
            self._resize()
        
        return True
    
    def modify(self, key, value):
        index = self._hash(key)
        start_index = index
        
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return True
            index = (index + 1) % self.cap
            if index == start_index:
                return False
        
        return False
    
    def remove(self, key):
        index = self._hash(key)
        start_index = index
        
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                self.size -= 1
                
                # Rehash the following elements
                next_index = (index + 1) % self.cap
                while self.table[next_index] is not None:
                    k, v = self.table[next_index]
                    self.table[next_index] = None
                    self.size -= 1
                    self.insert(k, v)
                    next_index = (next_index + 1) % self.cap
                
                return True
            index = (index + 1) % self.cap
            if index == start_index:
                return False
        
        return False
    
    def search(self, key):
        index = self._hash(key)
        start_index = index
        
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.cap
            if index == start_index:
                return None
        
        return None
    
    def capacity(self):
        return self.cap
    
    def __len__(self):
        return self.size
