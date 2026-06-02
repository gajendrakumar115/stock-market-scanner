import pandas as pd
import yfinance as yf
from indicators import calculate_rsi

def scan_stocks(stock_list):
    results = []
    for symbol in stock_list:
        data = yf.Ticker(symbol).history(period="3mo")

        data["RSI"] = calculate_rsi(data)


        latest_close = data["Close"].iloc[-1]
        latest_rsi = data["RSI"].iloc[-1]

        momentum = (
                           (data["Close"].iloc[-1] -
                            data["Close"].iloc[-20])
                           /
                           data["Close"].iloc[-20]
                   ) * 100

        if latest_rsi < 60 and momentum > 3:
            signal = "BUY"

        elif latest_rsi > 70:
            signal = "SELL"

        else:
            signal = "HOLD"

        results.append({
            "symbol": symbol,
            "Price": round(latest_close,2),
            "RSI": round(latest_rsi,2),
            "Momentum": round(momentum, 2),
            "Signal": signal

        })
    return pd.DataFrame(results)