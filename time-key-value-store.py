class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []

        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        values = self.store.get(key, [])

        left, right = 0, len(values) - 1

        while left <= right:
            mid = (left + right) // 2
            if values[mid][0] <= timestamp:
                result = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1
            
        return result

# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
obj.set("foo","bar",1)
print(obj.get("foo",1))
print(obj.get("foo",3))
obj.set("foo","bar2",4)
print(obj.get("foo",4))
print(obj.get("foo",5))

