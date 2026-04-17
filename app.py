import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# ----------------------------
# Input
# ----------------------------
ticker = input("Enter stock ticker (e.g., AAPL, TCS.NS): ").upper().strip()
period = input("Enter period (1mo, 3mo, 6mo, 1y): ").strip()

# ----------------------------
# Fetch Data
# ----------------------------
print("\nFetching stock data...")

data = yf.download(ticker, period=period)

# Handle MultiIndex issue
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.droplevel(1)

# ----------------------------
# Validate Data
# ----------------------------
if data.empty:
    print("⚠️ No data found. Please check the ticker or try again.")
    exit()

# ----------------------------
# Plot Graph
# ----------------------------
plt.figure(figsize=(10, 5))

plt.plot(data.index, data["Close"], marker="o", linewidth=2)

plt.title(f"{ticker} Stock Price")
plt.xlabel("Date")
plt.ylabel("Price")

plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()
plt.show()

# ----------------------------
# Calculations
# ----------------------------
highest_price = float(data["High"].max())
lowest_price = float(data["Low"].min())

start_price = float(data["Close"].iloc[0])
end_price = float(data["Close"].iloc[-1])

percentage_change = ((end_price - start_price) / start_price) * 100

# ----------------------------
# Output
# ----------------------------
print("\n📊 Stock Summary")
print("-----------------------------")
print(f"Ticker: {ticker}")
print(f"Highest Price: ${highest_price:.2f}")
print(f"Lowest Price: ${lowest_price:.2f}")

if percentage_change >= 0:
    print(f"Percentage Change: {percentage_change:.2f}% 📈 Profit")
else:
    print(f"Percentage Change: {percentage_change:.2f}% 📉 Loss")