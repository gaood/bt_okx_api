from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

from datetime import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])
from data.data import Data
import backtrader as bt
from data.const import DATA_NAME, API_KEY, SECRET_KEY, PASSPHRASE
import pandas as pd
from strategys.sma_cross_strategy import SmaCrossStrategy


if __name__ == '__main__':
    
    # Create a cerebro entity
    cerebro = bt.Cerebro()
    # 添加策略
    cerebro.addstrategy(SmaCrossStrategy)
    cerebro.addsizer(bt.sizers.FixedSize, stake=100)
    # 获取数据
    # 币种
    instId = 'SOL-USDT'
    Data(API_KEY, SECRET_KEY, PASSPHRASE).get_candlesticks(instId)
    # 添加数据
    datapath = ('./data/'+instId+'.csv')
    data = bt.feeds.GenericCSVData(
        dataname = datapath,
        datetime=1,
        open=2,
        high=3,
        low=4,    
        close=5,
        volume=6,
        openinterest=-1
    )
    print(data)
    cerebro.adddata(data)

    # Set our desired cash start
    cerebro.broker.setcash(100000.0)
    
    # Print out the starting conditions
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # Run over everything
    cerebro.run()
    cerebro.plot()
    # Print out the final result
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
