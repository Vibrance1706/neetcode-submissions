class TimeMap:

    def __init__(self):
        self.timemap_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap_dict:
            self.timemap_dict[key] = []
        
        self.timemap_dict[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap_dict:
            return ""
        
        op =""
        for t, v in self.timemap_dict[key]:
            if t<=timestamp:
                op = v
            else:
                break
        
        return op
                
                    

