import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Title
st.title("📈 Stock Price Viewer")

# Sidebar options
st.sidebar.header("Options")

ticker = st.sidebar.selectbox(
    "Choose a stock",
    ["AAPL", "TSLA", "GOOGL", "MSFT", "TCS.NS"]
)

custom_ticker = st.sidebar.text_input("Or enter custom ticker")

if custom_ticker:
    ticker = custom_ticker.upper()

period = st.sidebar.selectbox(
    "Select period",
    ["1mo", "3mo", "6mo", "1y"]
)

# Fetch data
with st.spinner("Fetching stock data..."):
    data = yf.download(ticker, period=period)

# Fix MultiIndex issue (safe handling)
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.droplevel(1)

# Plot graph
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(data.index, data['Close'], marker='o')
ax.set_title(f"{ticker} Stock Price")
ax.set_xlabel("Date")
ax.set_ylabel("Price")
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)

# Calculate metrics safely
highest_price = float(data['High'].max())
lowest_price = float(data['Low'].min())

start_price = float(data['Close'].iloc[0])
end_price = float(data['Close'].iloc[-1])

percentage_change = ((end_price - start_price) / start_price) * 100

# Display metrics
st.subheader("📌 Key Metrics")

col1, col2, col3 = st.columns(3)

col1.metric("Highest Price", f"{highest_price:.2f}")
col2.metric("Lowest Price", f"{lowest_price:.2f}")
col3.metric("Percentage Change", f"{percentage_change:.2f}%")