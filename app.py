import yfinance as yf
import matplotlib.pyplot as plt

stock = input("Enter stock symbol (e.g., AAPL, TCS.NS): ")

data = yf.download(stock, period="7d")

if data.empty:
    print("Invalid stock symbol or no data found.")
    exit()

plt.plot(data['Close'])
plt.title(f"{stock} Stock Price (Last 7 Days)")
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()

highest_price = data['High'].max()
lowest_price = data['Low'].min()

start_price = data['Close'].iloc[0]
end_price = data['Close'].iloc[-1]

percentage_change = ((end_price - start_price) / start_price) * 100

print("Highest Price:", round(highest_price, 2))
print("Lowest Price:", round(lowest_price, 2))
print("Percentage Change:", round(percentage_change, 2), "%")