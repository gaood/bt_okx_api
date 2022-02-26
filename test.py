import json
import okx.Market_api as Market

from data.data_cleaning import DataCleaning

if __name__ == '__main__':
    api_key = "a7e9547e-8415-49be-bbea-864a4190730b"
    secret_key = "ECD978632FB8CBD0BACA559281FF9A23"
    passphrase = "gaodi0226"


    # flag是实盘与模拟盘的切换参数 flag is the key parameter which can help you to change between demo and real trading.
    flag = '1'  # 模拟盘 demo trading
    # flag = '0'  # 实盘 real trading

   
    # market api
    marketAPI = Market.MarketAPI(api_key, secret_key, passphrase, False, flag)
    # 获取所有产品行情信息  Get Tickers
    # result = marketAPI.get_tickers('SPOT')
    # 获取单个产品行情信息  Get Ticker
    # result = marketAPI.get_ticker('BTC-USDT')
    # 获取指数行情  Get Index Tickers
    # result = marketAPI.get_index_ticker('BTC', 'BTC-USD')
    # 获取产品深度  Get Order Book
    # result = marketAPI.get_orderbook('BTC-USDT-210402', '400')
    # 获取所有交易产品K线数据  Get Candlesticks
    # result = marketAPI.get_candlesticks('BTC-USDT-210924', bar='1m')
    # 获取交易产品历史K线数据（仅主流币实盘数据）  Get Candlesticks History（top currencies in real-trading only）
    result = marketAPI.get_history_candlesticks('BTC-USDT')
    # 获取指数K线数据  Get Index Candlesticks
    # result = marketAPI.get_index_candlesticks('BTC-USDT')
    # 获取标记价格K线数据  Get Mark Price Candlesticks
    #result = marketAPI.get_markprice_candlesticks('BTC-USDT')
    # 获取交易产品公共成交数据  Get Trades
    # result = marketAPI.get_trades('BTC-USDT', '400')
    # 获取平台24小时成交总量  Get Platform 24 Volume
    # result = marketAPI.get_volume()
    # Oracle 上链交易数据 GET Oracle
    # result = marketAPI.get_oracle()
    # 获取指数成分数据 GET Index Components
    # result = marketAPI.get_index_components(index='')
    # 获取法币汇率 GET exchange rate in legal currency
    # result = marketAPI.get_exchange_rate()
    
    res = DataCleaning(result).toDataFrame()
    
    print(res)
    
