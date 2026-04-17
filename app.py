import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Input
ticker = input("Enter stock ticker (e.g., AAPL, TCS.NS): ").upper()
period = input("Enter period (7d, 1mo, 3mo, 6mo): ")

# Fetch data
data = yf.download(ticker, period=period)

# Fix MultiIndex
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.droplevel(1)

if not data.empty:

    # Plot
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data['Close'], marker='o')

    plt.title(f"{ticker} Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Price")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Calculations
    highest_price = float(data['High'].max())
    lowest_price = float(data['Low'].min())

    start_price = float(data['Close'].iloc[0])
    end_price = float(data['Close'].iloc[-1])

    percentage_change = ((end_price - start_price) / start_price) * 100

    # Output
    print("\n--- Stock Summary ---")
    print(f"Highest Price: {highest_price:.2f}")
    print(f"Lowest Price: {lowest_price:.2f}")

    if percentage_change >= 0:
        print(f"Percentage Change: {percentage_change:.2f}% 📈 Profit")
    else:
        print(f"Percentage Change: {percentage_change:.2f}% 📉 Loss")

else:
    print("❌ Invalid ticker or no data found")