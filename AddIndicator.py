##############################################################################################################
# This is the function to add new indicators in the Excel due to 
##############################################################################################################
from enum import unique
import backtrader as bt
import datetime
import pandas as pd
import numpy as np
import yfinance as yf
from yahoofinancials import YahooFinancials

# Read the source data file
securities_data = pd.read_csv("./data/SecurityData.csv")

# Have a overview
print(securities_data.head())

# The sucurities contained
securiteis_list = securities_data.loc[:, "sec_code"].unique()

print(securiteis_list)

