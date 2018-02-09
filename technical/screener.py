from abc import abstractmethod
import indicators as ind
import pandas as pd
import numpy as np


class Screener:
    strategies = []
    strategy_results = []

    def __init__(self, data):
        self.data = data

    def add_strategy(self, strategy):
        if strategy is None or not isinstance(strategy, Strategy):
            raise Exception('invalid strategy passed')

        self.strategies.append(strategy)

    def remove_strategy(self, strategy):
        if strategy is None or not isinstance(strategy, Strategy):
            raise Exception('invalid strategy passed')

        if strategy in self.stratagies:
            self.strategies.remove(strategy)

    def run(self):
        for strategy in self.strategies:
            self.strategy_results.append(strategy.execute())

        return self.strategy_results


class StrategyResult:
    weight = 1
    buy_sell = 'buy'
    strategy_name = None

    def __init__(self, name):
        self.strategy_name = name

    def set_sell(self):
        self.set_strategy('sell')

    def set_buy(self):
        self.set_strategy('buy')

    def set_watch(self):
        self.set_strategy('watch')

    def set_strategy(self, strategy):
        self.buy_sell = strategy

    def set_weight(self, weight):
        self.weight = weight


class Strategy(object):
    data = None
    strategy_name = None

    def __init__(self, data):
        if not isinstance(data, pd.DataFrame):
            raise Exception('Dataframe expected')

        self.data = data

    @abstractmethod
    def execute(self):
        pass

    @property
    @abstractmethod
    def output(self):
        pass


class EmaReversion(Strategy):

    @property
    def output(self):
        return self.min_sma, self.max_sma

    def __init__(self, data, name, min_period=0, max_period=0):

        if name is None:
            raise Exception('invalid parameters passed')

        if max_period == 0 or min_period == 0 or min_period > max_period:
            raise Exception('invalid parameters')

        super(EmaReversion, self).__init__(data)

        self.min_period = min_period
        self.max_period = max_period
        self.name = name
        self.strategy_name = 'Mean Reversion of periods: ' + str(self.min_period) + ' and ' + str(self.max_period)

    def execute(self):
        min_sma = ind.Ema(self.data, self.name, self.min_period)
        max_sma = ind.Ema(self.data, self.name, self.max_period)

        strat_result = StrategyResult(self.strategy_name)

        curr_price = self.data[self.name][-1]

        if min_sma[-1] > max_sma[-1] and min_sma[-2] < max_sma[-2]:
            strat_result.set_buy()
        elif min_sma[-1] < max_sma[-1] and min_sma[-2] > max_sma[-2]:
            strat_result.set_sell()
        elif min_sma[-1] > max_sma[-1] and (curr_price > min_sma[-1] or curr_price > max_sma[-1]):
            strat_result.set_strategy('watch and buy')
        elif min_sma[-1] < max_sma[-1] and (curr_price < min_sma[-1] or curr_price < max_sma[-1]):
            strat_result.set_strategy('sell')

        wt = (curr_price - max_sma[-1]) / (min_sma[-1] - max_sma[-1])
        strat_result.set_weight(wt)

        self.min_sma = min_sma
        self.max_sma = max_sma

        return strat_result


class Bollinger(Strategy):

    @property
    def output(self):
        self.rolling_agg['up_std'] = self.rolling_agg['mean'] + self.rolling_agg['std'] * self.nstds
        self.rolling_agg['low_std'] = self.rolling_agg['mean'] - self.rolling_agg['std'] * self.nstds
        return self.rolling_agg

    def __init__(self, data, name, period, nstds=1):
        super(Bollinger, self).__init__(data)
        self.period = period
        self.name = name
        self.nstds = nstds
        self.strategy_name = 'Bollinger bands for rolling period: ' + str(self.period)

    def execute(self):

        rolling_agg = self.data[self.name].rolling(self.period).agg([np.mean, np.std])

        strategy_result = StrategyResult(self.strategy_name)

        curr_price = self.data[self.name][-1]

        current_mean = rolling_agg['mean'][-1]
        upper_sd = current_mean + rolling_agg['std'][-1] * self.nstds
        lower_sd = current_mean - rolling_agg['std'][-1] * self.nstds

        if curr_price > upper_sd:
            strategy_result.set_sell()
        elif curr_price < lower_sd:
            strategy_result.set_buy()

        wt = (curr_price - lower_sd) / (upper_sd - lower_sd)

        strategy_result.set_weight(wt)

        self.rolling_agg = rolling_agg

        return strategy_result


class StochasticOscillator(Strategy):

    @property
    def output(self):
        return self.K, self.D

    def __init__(self, data, k_period=14, d_period=3, name='close'):
        super(StochasticOscillator, self).__init__(data)
        self.period = k_period
        self.d_period = d_period
        self.name = name
        self.strategy_name = 'Stochastic oscillator for period ' + str(self.period)

    def execute(self):

        data_col = self.data

        K = 100 * (data_col[self.name] - data_col[self.name].rolling(self.period).min()) / (
                data_col[self.name].rolling(self.period).max() - data_col[self.name].rolling(self.period).min())
        D = K.rolling(self.d_period).mean()

        strg = StrategyResult(self.strategy_name)

        strg.set_weight(K[-1])

        if K[-1] > 80:
            strg.set_sell()
        elif K[-1] < 20:
            strg.set_buy()
        else:
            strg.set_watch()

        self.K = K
        self.D = D

        return strg


class Macd(Strategy):

    def __init__(self, data, name, min_period=12, max_period=21, signal_period=7):
        super(Macd, self).__init__(data)
        self.name = name
        self.min_period = min_period
        self.max_period = max_period
        self.signal_period = signal_period
        self.macd = None
        self.signal = None
        self.strategy_name = 'Macd (' + str(self.min_period) + ',' + str(self.max_period) + ', signal : ' + str(
            self.signal_period) + ')'

    @property
    def output(self):
        return self.macd, self.signal

    def execute(self):
        ema_min = pd.ewma(self.data[self.name], span=self.min_period)
        ema_max = pd.ewma(self.data[self.name], span=self.max_period)

        macd = ema_min - ema_max
        signal = pd.ewma(macd, span=self.signal_period)

        self.macd = macd
        self.signal = signal

        strg = StrategyResult(self.strategy_name)

        if macd[-2] < signal[-2] and macd[-1] > signal[-1]:
            strg.set_buy()
        elif macd[-2] > signal[-2] and macd[-1] < signal[-1]:
            strg.set_sell()
        elif macd[-1] > signal[-1]:
            strg.set_strategy('watch and buy')
            strg.set_weight(macd[-1] / signal[-1])
        elif macd[-1] < signal[-1]:
            strg.set_strategy('sell')
            strg.set_weight(signal[-1] / macd[-1])

        return strg


class Vwap(Strategy):

    def __init__(self, data, name, period=14, vol_col_name='volume'):
        super(Vwap, self).__init__(data)
        self.period = period
        self.name = name
        self.vol_col = vol_col_name

    @property
    def output(self):
        pass

    def execute(self):
        vwd = self.vwap(self.data[-self.period:][self.name], self.data[-self.period:][self.vol_col])

        close_price = self.data[self.name][-1]
        strategy_result = StrategyResult('VWAP')

        wt = (close_price / vwd) - 1
        if wt > 0:
            strategy_result.set_strategy(
                'Current price : ' + str(close_price) + ' is greater than VWAP Price :' + str(vwd) + ' by ' + str(
                    (wt * 100)) + '%')

        else:
            strategy_result.set_strategy(
                'Current price : ' + str(close_price) + 'is less than VWAP Price :' + str(vwd) + ' by ' + str(
                    (1 + wt) * 100) + '%')

        strategy_result.set_weight(wt * 100)

        return strategy_result

    def vwap(self, price_data, volume_data):
        vwap_data = (price_data * volume_data).sum() / volume_data.sum()
        return vwap_data


class Rsi(Strategy):

    def __init__(self, data, name='close', period=14):
        super(Rsi, self).__init__(data)
        self.period = period
        self.name = name

    def gtzero(self, x, default=0):
        if x > 0:
            return x
        else:
            return default

    def ltzero(self, x, default=0):
        if x < 0:
            return x
        else:
            return default

    def execute(self):
        diff = self.data[self.name] - self.data[self.name].shift(1)

        up = diff.apply(lambda x: self.gtzero(x))
        down = diff.apply(lambda x: -self.ltzero(x))

        print(up)
        print(down)

        # up = np.where(diff > 0, diff, 0)
        # down = np.where(diff > 0, 0, -diff)

        up_avg = up.rolling(self.period).mean()
        down_avg = down.rolling(self.period).mean()

        relative_strength = up_avg / down_avg

        rsi = 100 - (100 / (relative_strength + 1))

        self.rsi = rsi

        strategy_result = StrategyResult('RSI')
        if rsi[-1] < 20:
            strategy_result.set_buy()
        elif rsi[-1] >= 80:
            strategy_result.set_sell()

        strategy_result.set_weight(rsi[-1])

        return strategy_result

    @property
    def output(self):
        return self.rsi
