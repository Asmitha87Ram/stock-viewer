import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Title
st.title("📈 Stock Price Viewer")

# Input
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TCS.NS)", "AAPL")

# Fetch data
data = yf.download(ticker, period="7d")

if not data.empty:

    # Plot graph
    fig, ax = plt.subplots(figsize=(12, 5))  # ✅ wider graph

    ax.plot(data.index, data['Close'], marker='o')

    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.set_title(f"{ticker} Stock Price")

    # ✅ FIXED DATE HANDLING (AUTO spacing)
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%b'))

    plt.xticks(rotation=45, ha='right')  # ✅ better alignment
    plt.tight_layout()  # ✅ prevents overlap

    st.pyplot(fig)

    # Calculate values
    highest_price = data['High'].max()
    lowest_price = data['Low'].min()

    start_price = data['Close'].iloc[0]
    end_price = data['Close'].iloc[-1]

    percentage_change = ((end_price - start_price) / start_price) * 100

    # Display results
    st.write(f"**Highest Price:** {highest_price:.2f}")
    st.write(f"**Lowest Price:** {lowest_price:.2f}")
    st.write(f"**Percentage Change:** {percentage_change:.2f}%")

else:
    st.error("Invalid ticker or no data found.")