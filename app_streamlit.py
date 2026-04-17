import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

st.title("📈 Stock Price Viewer")

stock = st.text_input("Enter stock symbol (e.g., AAPL, TCS.NS)")

if stock:
    data = yf.download(stock, period="7d")

    if data.empty:
        st.error("Invalid stock symbol")
    else:
        st.subheader(f"{stock} Stock Price (Last 7 Days)")

        fig, ax = plt.subplots()
        ax.plot(data['Close'])
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        st.pyplot(fig)

        highest_price = data['High'].max().item()
        lowest_price = data['Low'].min().item()

        start_price = data['Close'].iloc[0]
        end_price = data['Close'].iloc[-1]

        percentage_change = ((end_price - start_price) / start_price) * 100
        percentage_change = percentage_change.item()

        st.write(f"**Highest Price:** {highest_price:.2f}")
        st.write(f"**Lowest Price:** {lowest_price:.2f}")
        st.write(f"**Percentage Change:** {percentage_change:.2f}%")