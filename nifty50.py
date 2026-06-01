import pandas as pd

def get_nifty50_stocks():
    try:
        url = "https://archives.nseindia.com/content/indices/ind_nifty50list.csv"

        df = pd.read_csv(url)

        return [symbol + ".NS" for symbol in df["Symbol"]]

    except Exception as e:
        print("Error fetching NIFTY50:", e)
        return []

