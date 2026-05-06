class MyHashMap:

    def __init__(self):
        self.keys = []
        self.values = []

    def put(self, key: int, value: int) -> None:
        if key not in self.keys:
            # print('adding: ', key, value)
            self.keys.append(key)
            self.values.append(value)
            # print(self.keys)
            # print(self.values)
        else:
            current_index = self.keys.index(key)
            self.values[current_index] = value

        

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1
        else:
            current_index = self.keys.index(key)
            return self.values[current_index]
        

    def remove(self, key: int) -> None:
        if key not in self.keys:
            return None
        else:
            current_index_key = self.keys.index(key)
            self.keys.pop(current_index_key)
            self.values.pop(current_index_key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)