import yfinance as yf
import matplotlib.pyplot as plt

# Choose stock
ticker = "AAPL"

# Fetch data
data = yf.download(ticker, period="1mo")

# Plot closing price
plt.figure(figsize=(10, 5))
plt.plot(data['Close'], marker='o')
plt.title(f"{ticker} Stock Price")
plt.xlabel("Date")
plt.ylabel("Price")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()

# Calculate metrics
highest_price = float(data['High'].max())
lowest_price = float(data['Low'].min())

start_price = float(data['Close'].iloc[0])
end_price = float(data['Close'].iloc[-1])

percentage_change = ((end_price - start_price) / start_price) * 100

# Print results
print(f"Highest Price: {highest_price:.2f}")
print(f"Lowest Price: {lowest_price:.2f}")
print(f"Percentage Change: {percentage_change:.2f}%")