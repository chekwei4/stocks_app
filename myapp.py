import yfinance as yf
import streamlit as st
from datetime import datetime
from datetime import datetime, timedelta
import datetime as dt
import pandas as pd
from datetime import time, date
from dateutil.relativedelta import relativedelta
from PIL import Image

st.set_page_config(layout="wide", page_title="Chek's Stonk App")
image = Image.open('cover.jpeg')
# st.image(image)
st.write("# My Stonk Price App")

def main():
    stock_input = st.text_input("Stock Ticker: ", "TSLA")
    today = date.today()
    data = yf.Ticker(stock_input).history()
    try:
        if 'Empty DataFrame' in str(data):
            raise Exception(f'We did not find results for: {stock_input}')
        else: 
            #using slider option
            date_range = st.slider(label="Date Range:", min_value=today - relativedelta(years=+1),value=(date(2021, 1, 1), today))
            start_date = date_range[0]
            end_date = date_range[1]

            #using button options
            col0, col1, col2, col3, col4, col5, col6  = st.columns([0.1,0.1,0.10,0.10,0.10,0.10,0.10])
            one_day = col0.button("1D")
            five_day = col1.button("5D")
            one_month = col2.button("1M")
            six_month = col3.button("6M")
            ytd = col4.button("YTD") #first day of calendar 
            one_year = col5.button("1Y")
            five_year = col6.button("5Y")
            
            if one_day:
                start_date = today - relativedelta(days=+2)
                end_date = today
            elif five_day:
                start_date = today - relativedelta(days=+5)
                end_date = today
            elif one_month:
                start_date = today - relativedelta(months=+1)
                end_date = today
            elif six_month:
                start_date = today - relativedelta(months=+6)
                end_date = today
            elif ytd:
                start_date = today.replace(month=1, day=1) 
                end_date = today
            elif one_year:
                start_date = today - relativedelta(years=+1)
                end_date = today
            elif five_year:
                start_date = today - relativedelta(years=+5)
                end_date = today

            # st.write("start:", start_date)
            # st.write("end:", end_date)
            data = yf.Ticker(stock_input).history(period="3mo", start=start_date,end=end_date)
            st.markdown(f"## Stock closing price and volume of {stock_input.upper()}")
            st.write("### Closing Price")
            st.line_chart(data.Close)
            st.write("### Volume")
            st.line_chart(data.Volume)
    except Exception as e:
        print(e)
        st.markdown(e)

if __name__ == "__main__":
    main()