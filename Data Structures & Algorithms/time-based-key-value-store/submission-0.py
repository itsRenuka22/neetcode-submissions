class TimeMap:

    def __init__(self):
        self.timeMap = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
        self.timeMap[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        l = 0
        arr = self.timeMap[key]
        r = len(arr) - 1
        res = ""

        while (l <= r):
            mid = (l + r) // 2

            if arr[mid][1] <= timestamp:
                res = arr[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return res
