class lru:

    def __init__(self,capacity):
        self.capacity = capacity
        self.cache = {}
        self.lru = []

    def get(self, key,default = None):
        if key in self.lru:
            return self.cache[key]
        return default

    def put(self, key):
        if len(self.lru) < self.capacity:
            if key in self.lru:
                self.lru.remove(key)
                self.lru.append(key)  
                self.cache[key]  = "Hello"+str(key)
            else:
                self.lru.append(key)
                self.cache[key] = "Hello"+str(key)
        else:
            
            r = self.lru.pop(0)
            self.lru.append(key)
            del self.cache[r]
            self.cache[key] = "Hello"+ str(key)
            
            
    def get_cache(self):
        lists = []
        for key in reversed(self.lru):
            lists.append(key +"____"+ self.cache[key])
        return lists
                    
        
    