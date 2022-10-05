import datetime
import backtrader as bt
import quantstats
import pandas as pd

#Instantiate Cerebro engine
cerebro = bt.Cerebro(stdstats=False)

#Set data parameters and add to Cerebro
data1 = bt.feeds.YahooFinanceCSVData(
    dataname='TSLA.csv',
    fromdate=datetime.datetime(2021, 1, 1),
    todate=datetime.datetime(2022, 10, 1))
cerebro.adddata(data1)

data2 = bt.feeds.YahooFinanceCSVData(
    dataname='AAPL.csv',
    fromdate=datetime.datetime(2021, 1, 1),
    todate=datetime.datetime(2022, 10, 1))

data2.compensate(data1)  # let the system know ops on data1 affect data0
data2.plotinfo.plotmaster = data1
data2.plotinfo.sameaxis = True
cerebro.adddata(data2)

cerebro.addanalyzer(bt.analyzers.PyFolio, _name='PyFolio')
#result = cerebro.run()
results = cerebro.run()

strat = results[0]

portfolio_stats = strat.analyzers.getbyname('PyFolio')
returns, positions, transactions, gross_lev = portfolio_stats.get_pf_items()
returns.index = returns.index.tz_convert(None)

quantstats.reports.html(returns, output='stats.html', title='BTC Sentiment')