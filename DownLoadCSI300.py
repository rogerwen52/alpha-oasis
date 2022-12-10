
# Author Roger Wen
# Date: 2022-12-10
# This script is used to download CSI300 historical data, you can also change the "Panel" to download other data

import tushare as ts
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

#############################################################################
################################## Panel ####################################
#############################################################################
today = datetime.today().strftime('%Y%m%d')

index_code = '000300.SH'
index_start_date = '20221201'
index_end_date = '20221201'

# For download Symbols data
start_date = '20221201'
end_date = '20221201'

# Export to CSV or not
EXPORT = False
EXPORT_path = r'C:\Users\roger\OneDrive\Desktop\Factor Investing\symbol_data_all_' + today + '.xlsx'

if (EXPORT == True):
    print("We will export the CSV file to: " + EXPORT_path)
else:
    print("We will not expor the CSV file, only testing...")

#############################################################################
#############################################################################
#############################################################################

# Assign API
pro = ts.pro_api('6597630def49a761876f65a20565cf1a7a5d7c40bd84ea86ccdda426')

# Get Index Data (We want the component) at a specific date
def get_index_data(index_code, start_date, end_date):
    # Define first, otherwise errors may occur
    df = []
    #
    try :
        df = pro.index_weight(index_code=index_code, start_date=start_date, end_date=end_date)
    except : 
        #time.sleep(0.5)
        print('Download Succeed')
    else :
        print('Download Fail')

    return df

df = get_index_data(index_code=index_code, start_date=index_start_date, end_date=index_end_date) 

print(df)

# We only want the constituent code
con_code = df['con_code']

# Transfer it to "list"
symbols_code = con_code.tolist()

def download_append_symbol_data(ts_code, start_date, end_date):
    # Define 
    symbols_data = pd.DataFrame()

    # Get and Append individual symbol data
    for symbol_code in symbols_code:

        symbols_data_temp = pro.daily(ts_code=ts_code, start_date=start_date, end_date=end_date)
 
        symbols_data = symbols_data.append(symbols_data_temp)

    return symbols_data

def export_to_csv(symbol_data, EXPORT, EXPORT_path):
    if (EXPORT == True):
        symbols_data.to_csv(EXPORT_path)

# Call download_append_symbol_data
download_append_symbol_data(symbols_code, start_date, end_date)

# Call export_to_csv
export_to_csv(symbols_data, EXPORT, EXPORT_path)