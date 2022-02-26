import json
import okx.Market_api as Market
from data.data_cleaning import DataCleaning

class Data:
    
    def __init__(self, api_key, secret_key, passphrase, flag = '1'):
        self.api_key = api_key
        self.secret_key = secret_key
        self.passphrase = passphrase
        self.flag = flag
        self.marketAPI = Market.MarketAPI(
            self.api_key, 
            self.secret_key, 
            self.passphrase, 
            False, 
            self.flag)

    # 获取交易产品历史K线数据（仅主流币实盘数据）
    def get_history_candlesticks(self, 
                                instId='LINK-USDT',
                                after='', 
                                before='', 
                                bar='15m', 
                                limit='1000'):
        result = self.marketAPI.get_history_candlesticks(
            instId, after, before, bar, limit)
        
        return DataCleaning(result, instId).toDataFrame()
    # 获取所有交易产品K线数据

    def get_candlesticks(self,
                        instId = 'LINK-USDT', 
                        after='', 
                        before='', 
                        bar='15m', 
                        limit='300'):
        result = self.marketAPI.get_candlesticks(
            instId, after, before, bar, limit)
        print(result)
        return DataCleaning(result,instId).toDataFrame()





