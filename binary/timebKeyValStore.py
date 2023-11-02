class TimeMap:

    def __init__(self):
        self.keyStore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = [[value, timestamp]]
        else:
            self.keyStore[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        l = 0
        r = len(self.keyStore.get(key, []))-1

        while l<=r:
            mid =  (l+r) //2
            if int(self.keyStore[key][mid][1]) <= timestamp:
                res = self.keyStore[key][mid][0]
                l = mid +1
            else:
                r = mid -1
        return res