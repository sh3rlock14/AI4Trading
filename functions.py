import os
import matplotlib.pyplot as plt
import pandas as pd
pd.options.display.width = 1200

import matplotlib
matplotlib.rc('figure', figsize=(10,3), dpi=200)


def adjusted_close_symbols(symbols, date_range):
    """ Joins an empty DataFrame with index, with multiple stocks dataframes. """

    # dates is formatted as YYYY-MM-DD
    dates = pd.date_range(*date_range)

    # An empty dataframe
    df1 = pd.DataFrame(index=dates) # the dataframe only with the index

    for sym in symbols:
        path_to_file = os.path.join("data", "%s.csv" % sym)
        dfSYM = pd.read_csv(path_to_file, index_col="Date", parse_dates=True, usecols=["Date", "Adj Close"]) # na_values=['nan']
        dfSYM = dfSYM.rename(columns= {'Adj Close': sym})
        df1 = df1.join(dfSYM, how="inner")
    return df1

def prova():
    print("Prova!")