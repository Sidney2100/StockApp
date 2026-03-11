import streamlit as st
import yfinance as yf

st.title("Stock Price Web Application")

ticker = st.text_input("Enter stock ticker", "AAPL")
period = st.selectbox("Choose time period", ["5d", "1mo", "3mo", "6mo", "1y"])

if st.button("Show Stock Price"):
    data = yf.download(ticker, period=period)

    st.write("Stock Data")
    st.write(data)

    st.write("Closing Price Chart")
    st.line_chart(data["Close"])
