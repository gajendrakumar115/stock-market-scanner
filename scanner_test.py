from nifty50 import get_nifty50_stocks
from scanner import scan_stocks
from email_alert import send_email
from datetime import  datetime

scanner_df = scan_stocks(get_nifty50_stocks())

print(scanner_df)

buy_stocks = scanner_df[
    scanner_df["Signal"] == "BUY"
]

top_10 = buy_stocks.sort_values(
    by=["Momentum","RSI"],
    ascending=[False,True]
)

print("\n===== TOP 10 BY OPPORTUNITIES =====\n")

print(top_10.head(10))

file_name = (
    f"Top_Buy_Opportunities_"
    f"{datetime.now():%Y%m%d}.xlsx"
)

top_10.head(10).to_excel(
    file_name,
    index=False,)

send_email(file_name)