import streamlit as st
from nifty50 import get_nifty50_stocks
from scanner import scan_stocks
from datetime import datetime


st.set_page_config(
    page_title="Stock Scanner",
    page_icon="📈",
    layout="wide"
)


st.title("Stock Market Scanner")

st.caption(
    f"Last Updated: {datetime.now().strftime('%d-%m-%Y %H:%M')}"
)

st.markdown("""
### Created by Gajendra Kumar (GK)

Sr. Data Engineer | Stock Market Enthusiast

This dashboard scans NIFTY50 stocks and identifies Buy Opportunities.
""")

if st.button("🔄 Refresh Scanner"):
    st.rerun()

col1,col2,col3 = st.columns(3)

# Get NIFTY50
try:
    with st.spinner("Scanning NIFTY50 stocks..."):
        stocks = get_nifty50_stocks()
        scanner_df = scan_stocks(stocks)

except Exception as e:
    st.error(f"Error: {e}")
    st.stop()

# Update Metrics
buy_signals = len(scanner_df[scanner_df["Signal"] == "BUY"])
sell_signals = len(scanner_df[scanner_df["Signal"] == "SELL"])
hold_signals = len(scanner_df[scanner_df["Signal"] == "HOLD"])


col1.metric("Stocks Scanned", len(stocks))
col2.metric("Buy Signals", buy_signals)
col3.metric("Hold Signals", hold_signals)

st.divider()

st.subheader("Market Summary")

st.write(f"🟢 BUY Signals Found: {buy_signals}")
st.write(f"🟠 HOLD Signals Found: {hold_signals}")
st.write(f"🔴 SELL Signals Found: {sell_signals}")

st.subheader("📊 NIFTY50 Scanner Results")

def highlight_signal(val):
    if val == "BUY":
        return "background-color: green; color: white"
    elif val == "SELL":
        return "background-color: red; color: white"
    elif val == "HOLD":
        return "background-color: orange; color: white"
    return ""
scanner_df["Status"] = scanner_df["Signal"].map({
    "BUY": "🟢 BUY",
    "SELL": "🔴 SELL",
    "HOLD": "🟠 HOLD"
})

#st.dataframe(scanner_df, width="stretch")

styled_df = scanner_df.style.map(
    highlight_signal,
    subset=["Signal"]
)

st.dataframe(styled_df, width="stretch")

buy_stocks = scanner_df[
    scanner_df["Signal"] == "BUY"
]

top_10 = buy_stocks.sort_values(
    by=["Momentum", "RSI"],
    ascending=[False, True]
)

st.subheader("🔥 Top Buy Opportunities")

if not buy_stocks.empty:
    st.dataframe(
        buy_stocks.sort_values(
            by=["Momentum", "RSI"],
            ascending=[False, True]
        ),
        width="stretch"
    )
else:
    st.warning("No BUY opportunities found today.")