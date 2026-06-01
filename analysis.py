def analyze_stock(data):
    print("\n===== STOCK REPORT =====")

    print("Average Close:", round(data["Close"].mean(), 2))
    print("Highest Close:", round(data["Close"].max(), 2))
    print("Lowest Close:", round(data["Close"].min(), 2))

    latest = data.iloc[-1]

    print("\nLatest Close:", round(latest["Close"], 2))
    print("Latest MA_5:", round(latest["MA_5"], 2))
    print("Latest Signal:", latest["Signal"])