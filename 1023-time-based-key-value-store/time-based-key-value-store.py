class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        value = self.data[key]
        low = 0
        high = len(value) - 1
        result = ""
        while low <= high:
            mid = low + ((high - low) // 2)
            if value[mid][1] == timestamp:
                return value[mid][0]

            if value[mid][1] < timestamp:
                result = value[mid][0]
                low = mid + 1
            else:
                high = mid - 1

        return result


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
