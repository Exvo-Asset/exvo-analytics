import pandas as pd


def simple_moving_average(prices, window=5):
s = pd.Series(prices)
return s.rolling(window).mean().tolist()
