class Backtester:
def __init__(self):
self.trades = []


def run(self, prices):
# dummy: buy-and-hold
return {'return_pct': (prices[-1] / prices[0] - 1) * 100}
