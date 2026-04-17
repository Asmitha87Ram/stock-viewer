import yfinance as yf
import matplotlib.pyplot as plt

# Input
ticker = input("Enter stock ticker (e.g., AAPL, TCS.NS): ")

# Fetch data
data = yf.download(ticker, period="7d")

if not data.empty:

    # Plot graph
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data['Close'], marker='o')

    plt.title(f"{ticker} Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Price")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()

    # Calculate values (FIXED)
    highest_price = float(data['High'].max())
    lowest_price = float(data['Low'].min())

    start_price = float(data['Close'].iloc[0])
    end_price = float(data['Close'].iloc[-1])

    percentage_change = ((end_price - start_price) / start_price) * 100

    # Output results
    print(f"\nHighest Price: {highest_price:.2f}")
    print(f"Lowest Price: {lowest_price:.2f}")
    print(f"Percentage Change: {percentage_change:.2f}%")

else:
    print("Invalid ticker or no data found.")