class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.new_dict = {}

    def get(self, key: int) -> int:
        capacity = self.capacity
        new_dict = self.new_dict
        if key in new_dict:
            value = new_dict.pop(key)
            new_dict[key] = value
            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        capacity = self.capacity
        new_dict = self.new_dict
        if key in new_dict:
            new_dict.pop(key)
        elif len(new_dict) >= capacity:
            new_dict.pop(next(iter(new_dict)))
            
        new_dict[key] = value
        



