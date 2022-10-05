##############################################################################################################
# This is the function to download and clean the security data.
# Since I do not know whether backtrader already contains some security calculation, I will just keep the 
# basic function of downloading and cleaning the data.
##############################################################################################################

import backtrader as bt
import datetime
import pandas as pd
import numpy as np
import yfinance as yf
from yahoofinancials import YahooFinancials

# Construct Security Data Class
class SecurityData():
    
    # Capture Securities Numbers
    securities_count = 0

    # Define Security Data
    securities_data = []

    # Define Security Return
    securities_return = []
    
    def __init__(self, securities_list, start_date, end_date):
        self.securities_list = securities_list
        self.start_date = start_date
        self.end_date = end_date

        # Print Security List
        print(self.security_list)

        # Count the number of securities
        SecurityData.securities_count += 1

    def download_data(self):

        securities_data = pd.DataFrame()

        for sec in self.security_list:
            # Download the data from yahoo.com, reset the index to make "Date" not a index
            temp_data = yf.download(sec, start=self.start_date, end=self.end_date).reset_index()

            # Add "openinterest" column
            temp_data["openinterest"] = 0

            # Add "sec_code" column
            temp_data["sec_code"] = sec

            # Append securities data
            securities_data = securities_data.append(temp_data)

            print("Download Done!")

        # Rename the columns
        securities_data.rename(columns = {'Date':'datetime', 'Open':'open', 'High':'high', 'Low':'low', 'Close':'close', 'Adj Close':'adj_close', 'Volume': 'volume'}, inplace = True)
        
        return securities_data

if __name__ == "__main__":
    # Run
    run_SecurityData = SecurityData(["AAPL", "TSLA"], "2017-01-01", "2021-12-31")

    # Get results
    securities_data_clean = run_SecurityData.download_data()

    # Print Results
    print(securities_data_clean)

    # Output to CSV
    print("Outputing to CSV...")
    securities_data_clean.to_csv("./data/SecurityData.csv", index = False)





     