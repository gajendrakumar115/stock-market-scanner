def generate_signals(data):

    data["Signal"] = ""

    for i in range(1, len(data)):

        if data["Close"].iloc[i] > data["Close"].iloc[i-1]:
            data.loc[data.index[i], "Signal"] = "BUY"
        else:
            data.loc[data.index[i], "Signal"] = "SELL"

    return data
