from collections import deque
import datetime


class HighLowTracker:
def __init__(self, window_seconds: int):
self.window = window_seconds
self.store = {} # symbol -> deque of (ts, price)


def add_snapshot(self, symbol: str, ts: datetime.datetime, price: float):
if symbol not in self.store:
self.store[symbol] = deque()
q = self.store[symbol]
q.append((ts, price))
# pop old
cutoff = ts - datetime.timedelta(seconds=self.window)
while q and q[0][0] < cutoff:
q.popleft()


def high_low(self, symbol: str):
q = self.store.get(symbol, [])
if not q:
return None, None
prices = [p for (_, p) in q]
return max(prices), min(prices)
