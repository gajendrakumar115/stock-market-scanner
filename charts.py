import matplotlib.pyplot as plt

def plot_stock(data):
    plt.figure(figsize=(10,5))

    plt.plot(data.index, data["Close"], label="Close Price")
    plt.plot(data.index, data["MA_5"], label="5_Day MA")

    buy = data[data["Signal"] == "BUY"]
    sell = data[data["Signal"] == "SELL"]

    plt.scatter(buy.index, buy["Close"], marker="^", s=100, label="BUY")
    plt.scatter(sell.index, sell["Close"], marker="v", s=100, label="SELL")

    plt.legend()
    plt.title("Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Price")

    plt.show()
