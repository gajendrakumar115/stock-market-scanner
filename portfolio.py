import yfinance as yf
import pandas as pd
from indicators import calculate_rsi
from screener import screen_stocks
from portfolio_charts import (
    plot_price_chart,
    plot_investment_chart,
    plot_allocation_chart
)


stocks = [
"TCS.NS",
    "RELIANCE.NS",
    "INFY.NS",
    "SBIN.NS",
    "HDFCBANK.NS"
]

print("\n===== PORTFOLIO =====\n")

results = []

for symbol in stocks:
    data = yf.Ticker(symbol).history(period="3mo")

    data["MA_5"] = data["Close"].rolling(5).mean()

    data["RSI"] = calculate_rsi(data)

    latest_close = data["Close"].iloc[-1]
    daily_change = (
        (data["Close"].iloc[-1] - data["Close"].iloc[-2])
        / data["Close"].iloc[-2]
    ) * 100

    latest_ma = data["MA_5"].iloc[-1]

    latest_rsi = data["RSI"].iloc[-1]

    if latest_rsi > 70:
        risk = "HIGH"
    elif latest_rsi < 30:
        risk = "LOW"
    else:
        risk = "MEDIUM"

    if latest_close > latest_ma:
        signal = "BUY"
    else:
        signal = "SELL"

    results.append({
         "Symbol": symbol,
         "Price" : round(latest_close, 2),
         "Daily Change %" : round(daily_change, 2),
         "RSI" : round(latest_rsi, 2),
         "RISK" : risk,
         "Signal" : signal,
         "Quantity": 10
    })

portfolio_df = pd.DataFrame(results)

print(portfolio_df)

portfolio_df["Investment Value"] = (
    portfolio_df["Price"] *
    portfolio_df["Quantity"]
)

## Portfolio Allocation %

portfolio_df["Portfolio %"] = round(
        (
    portfolio_df["Investment Value"]
    / portfolio_df["Investment Value"].sum()
    ) * 100,
2)



print("\n===== PORTFOLIO REPORT =====\n")
print(portfolio_df)

## Sorting based on price


portfolio_df = portfolio_df.sort_values(
    by ="Price",
    ascending=False
)

print("\n===== PORTFOLIO Based On Sorting Price REPORT =====\n")
print(portfolio_df)

## Top Gainers

print("\n==== TOP GAINERS ====\n")

top_gainers = portfolio_df.sort_values(
    by ="Daily Change %",
    ascending=False
)

print(top_gainers.head(3))


## Top Losers

print("\n==== TOP LOSERS ====\n")

top_gainers = portfolio_df.sort_values(
    by ="Daily Change %",
    ascending=True
)

print(top_gainers.head(3))

### BUY signal

by_stocks = portfolio_df[portfolio_df["Signal"]=="BUY"]
print("\n===== BUY STOCKS =====\n")
print(by_stocks)



## csv export

portfolio_df.to_csv("portfolio_report.csv",
                    index=False,
                    )
print("\n===== Report Saved Scuccesfully =====\n")

## Portfolio Bar Chart

total_value = portfolio_df["Investment Value"].sum()

print("\n===== Total Value =====\n")

print(f"Total Portfolio Value: ₹{total_value:,.2f}")

print("\n===== PORTFOLIO ALLOCATION =====\n")

print(
    portfolio_df[
        ["Symbol",
         "Investment Value",
         "Portfolio %"]
    ]
)

plot_price_chart(portfolio_df)

plot_investment_chart(portfolio_df)

plot_allocation_chart(portfolio_df)

## STOCK SCREENER

screen_stocks(portfolio_df)


## Portfolio Ranking

portfolio_df["Rank"] = (
    portfolio_df["Investment Value"]
    .rank(ascending=False)
    .astype(int)
)

print("\n===== PORTFOLIO RANKING====\n")
print(
    portfolio_df[
        ["Rank","Symbol", "Investment Value"]
    ].sort_values("Rank")
)
