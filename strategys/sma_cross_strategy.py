from datetime import datetime
import backtrader as bt
import backtrader.feeds as btfeeds


class SmaCrossStrategy(bt.SignalStrategy):


    params = (('period', 30),)

    def __init__(self):
        self.sma = bt.indicators.SimpleMovingAverage(period=self.p.period)

    def notify_order(self, order):
        print("\033[31mbar序：{}，订单通知 size:{},price:{},pricelimit:{},exectype:{},tradeid:{},status:{}\033[0m"
              .format(len(self), order.size,order.price,order.pricelimit,order.ExecTypes[order.exectype],order.tradeid,order.Status[order.status]))

        if not order.alive():
            self.order = None

    def notify_trade(self, trade):
        print("\033[32mbar序：{}，交易通知 size:{},price:{},value:{},tradeid:{},status:{}\033[0m"
              .format(len(self), trade.size,trade.price,trade.value,trade.tradeid,trade.status_names[trade.status]))

    '''def notify_cashvalue(self, cash, value):
        print("\033[33mbar序：{}，资产通知 cash:{},value:{}\033[0m"
              .format(len(self),cash,value))'''

    def start(self):
        self.order = None

    def next(self):
        #print("bar序：{}，next sma={},close={}".format(len(self),self.sma[0],self.data.close[0]))
        if self.order:
            return

        if not self.position:
            if self.sma > self.data.close:
                self.order = self.order_target_percent(target=1.0, price=self.data.close[0]*0.99, exectype=bt.Order.Limit)
                #self.order = self.buy(price=self.data.close[0]*0.99,exectype=bt.Order.Limit)
        else:
            if self.sma < self.data.close:
                self.close()
