
import datetime  # For datetime objects
import os.path  # To manage paths
import sys  # To find out the script name (in argv[0])

# Import the backtrader platform
import backtrader as bt
import yfinance as yf
from yahoofinancials import YahooFinancials

'''
if __name__ == '__main__':
    # Create a cerebro entity
    cerebro = bt.Cerebro()

    data = bt.feeds.PandasData(dataname=yf.download('TSLA', '2018-01-01', '2019-01-01'))

    # Add the Data Feed to Cerebro
    cerebro.adddata(data)

    # Set our desired cash start
    cerebro.broker.setcash(100000.0)

    # Print out the starting conditions
    print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())

    # Run over everything
    cerebro.run()

    print(data[0].close)
    # Print out the final result
    print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())



    strategies = cerebro.run()
'''

class PrintClose(bt.Strategy):

    def __init__(self):
        #Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        
    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print(dt)

    def next(self):
		self.log('Close: ', self.dataclose[0])

#Instantiate Cerebro engine
cerebro = bt.Cerebro()

#Add data feed to Cerebro
data = bt.feeds.PandasData(dataname=yf.download('TSLA', '2018-01-01', '2019-01-01'))
cerebro.adddata(data)

#Add strategy to Cerebro
cerebro.addstrategy(PrintClose)

#Run Cerebro Engine
cerebro.run()
