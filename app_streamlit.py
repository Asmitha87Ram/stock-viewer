import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

# Title
st.title("📊 Advanced Stock Price Viewer")

# Sidebar
st.sidebar.header("Options")

stock_options = ["AAPL", "GOOGL", "MSFT", "TSLA", "TCS.NS"]
ticker = st.sidebar.selectbox("Choose a stock", stock_options)

custom_ticker = st.sidebar.text_input("Or enter custom ticker")

if custom_ticker:
    ticker = custom_ticker.upper()

period = st.sidebar.selectbox("Select period", ["7d", "1mo", "3mo", "6mo"])

# Fetch data
data = yf.download(ticker, period=period)

# 🔥 Fix MultiIndex issue
if isinstance(data.columns, pd.MultiIndex):
    data.columns = data.columns.droplevel(1)

if not data.empty:

    # Plot graph
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(data.index, data['Close'], marker='o')

    ax.set_title(f"{ticker} Stock Price")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")

    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%b'))

    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    st.pyplot(fig)

    # Calculations
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

    # Color change
    if percentage_change >= 0:
        col3.metric("Change", f"{percentage_change:.2f}%", delta="Profit 📈")
    else:
        col3.metric("Change", f"{percentage_change:.2f}%", delta="Loss 📉")

else:
    st.error("❌ Invalid ticker or no data found")