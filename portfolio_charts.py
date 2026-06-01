import matplotlib.pyplot as plt


def plot_price_chart(portfolio_df):

    plt.figure(figsize=(10, 5))

    plt.bar(
        portfolio_df["Symbol"],
        portfolio_df["Price"]
    )

    plt.title("Portfolio Stock Prices")
    plt.xlabel("Stock")
    plt.ylabel("Price")

    plt.show()


def plot_investment_chart(portfolio_df):

    plt.figure(figsize=(10, 5))

    plt.bar(
        portfolio_df["Symbol"],
        portfolio_df["Investment Value"]
    )

    plt.title("Investment Value")
    plt.xlabel("Stock")
    plt.ylabel("Investment Value (₹)")

    plt.show()


def plot_allocation_chart(portfolio_df):

    plt.figure(figsize=(8, 8))

    plt.pie(
        portfolio_df["Investment Value"],
        labels=portfolio_df["Symbol"],
        autopct="%1.1f%%"
    )

    plt.title("Portfolio Allocation")

    plt.show()