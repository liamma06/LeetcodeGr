class RecentCounter:

    def __init__(self):
        self.records= []
        self.counter = 0
        

    def ping(self, t: int) -> int:
        self.records.append(t)
        while self.records[self.counter] < t -3000:
            self.counter += 1
        return len(self.records) -self.counter



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)