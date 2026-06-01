def generate_signals(data):

    data["Signal"]=""

    for i in range(5,len(data)):
        if data["Close"].iloc[i]>data["Close"].iloc[i]:
            data.loc[data.index[i], "Signal"] = "Buy"
        else:
            data.loc[data.index[i], "Signal"]= "Sell"

    return data
