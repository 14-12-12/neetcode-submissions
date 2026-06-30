from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.hashmap = {}
        self.least = deque()
        self.store = {}
    def get(self, key: int) -> int:
        if key in self.hashmap:
            self.update(key)
            return self.hashmap[key]
        return -1
    def put(self, key: int, value: int) -> None:
        if self.get(key) == -1:
            if(self.size == self.capacity):
                self.remove()
                self.hashmap[key] = value 
                self.size += 1
                self.update(key)
            else:
                self.hashmap[key] = value 
                self.size += 1
                self.update(key)
        else:
            self.hashmap[key] = value
            self.update(key)

    def update(self, key:int):
        if key not in self.store:
            self.least.append(key)
            self.store[key] = len(self.least)-1
            print(self.store)
            print(self.least)
        else:
            idx = self.store[key]
            self.least[idx] = -1
            self.least.append(key)
            self.store[key] = len(self.least)-1

    def remove(self)-> None:
        value = self.least[0]
        temp = self.capacity -1
        i = 0
        while(self.size != temp):
            if value in self.hashmap:
                del self.hashmap[value]
                self.size -= 1
            else:
                i = i+1
                value = self.least[i]

            




        
