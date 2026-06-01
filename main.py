import yfinance as yf
from charts import plot_stock
from strategy import generate_signals
from analysis import analyze_stock

symbol = "TCS.NS"
stock = yf.Ticker(symbol)
print("Analyzing:", symbol)

data = stock.history(period="5mo")
data["MA_5"] = data["Close"].rolling(5).mean()

# BUY/SELL logic
data = generate_signals(data)

# reports
analyze_stock(data)

# graphs
plot_stock(data)

