import streamlit as st
import yfinance as yf

# Streamlit app title
st.title("Stock News Fetcher")

# Input box for stock symbol
stock_symbol = st.text_input("Enter Stock Symbol (e.g., AAPL):", "AAPL")

# Submit button
if st.button("Fetch News"):
    if stock_symbol:
        # Fetch stock data using yfinance
        stock = yf.Ticker(stock_symbol)
        
        # Fetch news
        news = stock.news
        
        if news:
            st.subheader(f"Latest News for {stock_symbol}")
            for item in news:
                content = item['content']
                # Display title
                st.write(f"**{content['title']}**")
                
                # Display publication date
                pub_date = content.get('pubDate', 'N/A')
                st.write(f"*Published on: {pub_date}*")
                
                # Display description (rendered as HTML)
                description = content.get('description', 'No description available.')
                st.markdown(description, unsafe_allow_html=True)

                if description == "":
                    summary = content.get('summary', 'No summary available.')
                    st.write(f"{summary}")
                
                # Display link to the full article
                link = content.get('previewUrl', '#')
                st.write(f"[Read more]({link})")
                
                # Add a separator
                st.write("---")
        else:
            st.warning(f"No news found for {stock_symbol}.")
    else:
        st.error("Please enter a valid stock symbol.")