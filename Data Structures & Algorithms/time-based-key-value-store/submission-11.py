class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.timeMap.get(key,[])
        value = ""
        l, r = 0, len(pairs) - 1

        while l <= r:
            mid = (r + l) // 2
            if pairs[mid][1] <= timestamp:
                value = pairs[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return value
        
