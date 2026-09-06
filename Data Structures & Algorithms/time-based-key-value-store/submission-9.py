class TimeMap:

    def __init__(self):
        self.dt = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dt[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.dt.get(key, 0)

        if timestamps == 0 or timestamp < timestamps[0][1]:
            return ""

        # if timestamp < timestamps[0][1]:
        #     return ""

        l, r = 0, len(timestamps) - 1

        while l < r:
            mid = l + (r - l + 1) // 2

            if timestamps[mid][1] <= timestamp:
                l = mid
            else:
                r = mid - 1

        

        return timestamps[l][0]