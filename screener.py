

def screen_stocks(df):

    print("\n===== STOCK SCREENER====\n")

    screened = df[
        (df["Signal"] == "BUY") &
        (df["RSI"] < 60)
    ]

    print(screened[
          ["Symbol", "Price", "RSI", "Signal"]
          ])