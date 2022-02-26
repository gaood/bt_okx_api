import pandas as pd
from data.const import DATA_NAME

class DataCleaning:
    def __init__(self,data,instId):
        self.data = data['data']
        self.instId = instId

    def toDataFrame(self):
        result = pd.DataFrame(self.data, columns=DATA_NAME)
        result['datetime'] = pd.to_datetime(
            result['datetime'],  unit='ms')
        path = 'data/' + self.instId + '.csv'
        return result.to_csv(path)
