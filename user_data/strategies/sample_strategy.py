from freqtrade.strategy import IStrategy
import pandas as pd
import talib.abstract as ta


class LokiSimple(IStrategy):
    """
    你的第一个最小可行策略（MVP）
    - 简单 EMA 趋势过滤
    - RSI 超卖/超买信号
    - 无复杂因子，保证可运行
    """

    timeframe = "1h"
    minimal_roi = {"0": 0.05}  # 简单止盈
    stoploss = -0.05

    def populate_indicators(self, df, metadata):

        # EMA 趋势线
        df["ema_fast"] = ta.EMA(df["close"], timeperiod=12)
        df["ema_slow"] = ta.EMA(df["close"], timeperiod=26)

        # RSI 信号
        df["rsi"] = ta.RSI(df["close"], timeperiod=14)

        return df

    def populate_buy_trend(self, df, metadata):
        df.loc[
            (
                (df["ema_fast"] > df["ema_slow"])  # 趋势向上
                & (df["rsi"] < 30)  # 超卖
            ),
            "buy",
        ] = 1

        return df

    def populate_sell_trend(self, df, metadata):
        df.loc[
            (
                (df["ema_fast"] < df["ema_slow"])  # 趋势反转
                | (df["rsi"] > 70)  # 超买
            ),
            "sell",
        ] = 1

        return df
