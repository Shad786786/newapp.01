import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Replace with full Nifty 150 symbols
nifty_150_symbols = [
    'RELIANCE.NS', 'TCS.NS', 'INFY.NS', 'HDFCBANK.NS', 'ICICIBANK.NS',
    'HINDUNILVR.NS', 'ITC.NS', 'KOTAKBANK.NS', 'LT.NS', 'SBIN.NS',
    'AXISBANK.NS', 'ASIANPAINT.NS', 'HCLTECH.NS', 'BAJFINANCE.NS', 'BHARTIARTL.NS',
    'MARUTI.NS', 'SUNPHARMA.NS', 'NTPC.NS', 'ULTRACEMCO.NS', 'NESTLEIND.NS',
    'POWERGRID.NS', 'TECHM.NS', 'TITAN.NS', 'WIPRO.NS', 'JSWSTEEL.NS',
    'ONGC.NS', 'COALINDIA.NS', 'TATACONSUM.NS', 'DIVISLAB.NS', 'GRASIM.NS',
    'ADANIENT.NS', 'ADANIPORTS.NS', 'HDFC.NS', 'BAJAJFINSV.NS', 'HEROMOTOCO.NS',
    'CIPLA.NS', 'BRITANNIA.NS', 'DRREDDY.NS', 'BPCL.NS', 'EICHERMOT.NS',
    'SHREECEM.NS', 'TATAMOTORS.NS', 'SBILIFE.NS', 'ICICIGI.NS', 'APOLLOHOSP.NS',
    'BAJAJ-AUTO.NS', 'M&M.NS', 'HDFCLIFE.NS', 'INDUSINDBK.NS', 'HINDALCO.NS',
    'AUROPHARMA.NS', 'GODREJCP.NS', 'ICICIPRULI.NS', 'LTI.NS', 'UBL.NS',
    'DMART.NS', 'NMDC.NS', 'HAVELLS.NS', 'BIOCON.NS', 'PIIND.NS',
    'VEDL.NS', 'NAUKRI.NS', 'ABB.NS', 'BANDHANBNK.NS', 'YESBANK.NS',
    'IDEA.NS', 'ADANIGREEN.NS', 'BAJAJHLDNG.NS', 'BERGEPAINT.NS', 'TORNTPHARM.NS',
    'CHOLAFIN.NS', 'SRF.NS', 'GAIL.NS', 'IGL.NS', 'MUTHOOTFIN.NS',
    'PAGEIND.NS', 'PETRONET.NS', 'SIEMENS.NS', 'TVSMOTOR.NS', 'TRENT.NS',
    'COLPAL.NS', 'LUPIN.NS', 'CANBK.NS', 'BANKBARODA.NS', 'MPHASIS.NS',
    'BEL.NS', 'ZYDUSLIFE.NS', 'FEDERALBNK.NS', 'DABUR.NS', 'BOSCHLTD.NS',
    'HINDPETRO.NS', 'AMBUJACEM.NS', 'INDIGO.NS', 'ACC.NS', 'INDUSTOWER.NS',
    'IDFCFIRSTB.NS', 'LICI.NS', 'PFC.NS', 'SHRIRAMFIN.NS', 'HAL.NS',
    'CONCOR.NS', 'CUMMINSIND.NS', 'BANKINDIA.NS', 'COROMANDEL.NS', 'LTIM.NS',
    'RECLTD.NS', 'SYNGENE.NS', 'HONAUT.NS', 'JUBLFOOD.NS', 'GUJGASLTD.NS',
    'APLLTD.NS', 'AARTIIND.NS', 'IRCTC.NS', 'VOLTAS.NS', 'GLAND.NS',
    'SAIL.NS', 'NHPC.NS', 'ZOMATO.NS', 'POLYCAB.NS', 'ATGL.NS',
    'TV18BRDCST.NS', 'BHEL.NS', 'IRFC.NS', 'IEX.NS', 'DELHIVERY.NS',
    'KPITTECH.NS', 'SJVN.NS', 'NAVINFLUOR.NS', 'ABBOTINDIA.NS'
]

# Streamlit app config
st.set_page_config(page_title="Nifty 125 Stock Data", layout="centered")
st.title("📊 Nifty 125 Stock Data Fetcher")

# Mode: Single Day or Full Month
mode = st.radio("Choose Fetch Mode", ["Single Day", "Full Month"])

# Input for Single Day
if mode == "Single Day":
    option = st.selectbox("Select Date Option:", ["Today", "Yesterday", "Custom"])
    if option == "Today":
        selected_date = datetime.today().date()
    elif option == "Yesterday":
        selected_date = (datetime.today() - timedelta(days=1)).date()
    else:
        selected_date = st.date_input("Pick a custom date", max_value=datetime.today())

# Input for Full Month
if mode == "Full Month":
    year = st.selectbox("Year", list(range(2020, datetime.today().year + 1)))
    month = st.selectbox("Month", list(range(1, 13)))
    start_date = datetime(year, month, 1)
    end_date = datetime(year + (month // 12), (month % 12) + 1, 1)

# Fetch Button
# Fetch Button
if st.button("📥 Fetch Data"):
    if mode == "Single Day":
        st.info(f"Fetching Nifty 125 data for {selected_date}...")
        all_data = []

        for symbol in nifty_150_symbols:
            try:
                ticker = yf.Ticker(symbol)
                hist = ticker.history(start=selected_date, end=selected_date + timedelta(days=1), interval="1d")
                if not hist.empty:
                    row = hist.iloc[0]
                    all_data.append({
                        "Date": selected_date,
                        "Symbol": symbol.replace(".NS", ""),
                        "Open": row["Open"],
                        "High": row["High"],
                        "Low": row["Low"],
                        "Close": row["Close"],
                        "Volume": row["Volume"]
                    })
            except Exception as e:
                st.warning(f"{symbol} failed: {e}")

        if all_data:
            df = pd.DataFrame(all_data)
            st.success(f"✅ Fetched {len(df)} rows.")
            st.dataframe(df)

            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button("⬇️ Download CSV", csv, file_name=f"nifty150_{selected_date}.csv", mime="text/csv")
        else:
            st.error("❌ No data found.")

    # ⬅️ FIXED: this 'elif' now correctly aligns with 'if mode == "Single Day"'
    elif mode == "Full Month":
        st.info(f"Fetching full month data for: {start_date.strftime('%B %Y')}")
        full_data = []

        for symbol in nifty_150_symbols:
            try:
                ticker = yf.Ticker(symbol)
                hist = ticker.history(start=start_date, end=end_date, interval="1d")
                for index, row in hist.iterrows():
                    full_data.append({
                        "Date": index.date(),
                        "Symbol": symbol.replace(".NS", ""),
                        "Open": row["Open"],
                        "High": row["High"],
                        "Low": row["Low"],
                        "Close": row["Close"],
                        "Volume": row["Volume"]
                    })
            except Exception as e:
                st.warning(f"{symbol} failed: {e}")

        if full_data:
            df_month = pd.DataFrame(full_data)

            df_month["Date"] = pd.to_datetime(df_month["Date"], format="%Y-%m-%d")
            df_month = df_month.sort_values(by=["Date", "Symbol"], ascending=[True, True])

            st.success(f"✅ Fetched {len(df_month)} rows.")
            st.dataframe(df_month.reset_index(drop=True))

            csv = df_month.to_csv(index=False).encode("utf-8")
            st.download_button(
                "⬇️ Download Monthly CSV",
                csv,
                file_name=f"nifty150_{year}_{month:02d}.csv",
                mime="text/csv"
            )
        else:
            st.error("❌ No data found for selected month.")
            # ✅ Power Finance Corporation Ltd. Section
st.header("📉 Power Finance Corporation Ltd. (PFC) Data")

col1, col2 = st.columns(2)
with col1:
    start_pfc = st.date_input("Start Date", datetime.now() - timedelta(days=30), key="start_pfc")
with col2:
    end_pfc = st.date_input("End Date", datetime.now(), key="end_pfc")

if st.button("📥 Fetch PFC Data"):
    with st.spinner("Fetching PFC data..."):
        symbol = "PFC.NS"
        isin = "INE134E01011"
        ticker = yf.Ticker(symbol)
        data = ticker.history(start=start_pfc, end=end_pfc + timedelta(days=1), interval="1d")

        if not data.empty:
            data.reset_index(inplace=True)
            data["Symbol"] = "PFC"
            data["ISIN"] = isin
            data = data[["Date", "Symbol", "ISIN", "Open", "High", "Low", "Close", "Volume"]]
            st.success(f"✅ Fetched {len(data)} rows of data.")
            st.dataframe(data)
            csv = data.to_csv(index=False).encode("utf-8")
            filename = f"PFC_{start_pfc}_to_{end_pfc}.csv"
            st.download_button("⬇️ Download CSV", csv, file_name=filename, mime="text/csv")
        else:
            st.warning("⚠️ No data available for the selected date range.")
            
            
            
            
            
            
            
            # --- Fetch F&O (Futures + Options) Data ---
from nsepython import nse_optionchain_scrapper

import streamlit as st
import pandas as pd
import requests
import time

st.set_page_config(page_title="Nifty Full Option Chain", layout="wide")
st.title("📊 Nifty Option Chain — Detailed Data with OI, IV, Bid/Ask")

symbol = "NIFTY"
def fetch_option_chain(symbol="NIFTY", retries=3):
    import requests
    import time

    url_home = "https://www.nseindia.com"
    url_api = f"https://www.nseindia.com/api/option-chain-indices?symbol={symbol}"

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/122.0.0.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://www.nseindia.com/option-chain",
        "Connection": "keep-alive",
    }

    session = requests.Session()
    session.headers.update(headers)

    for i in range(retries):
        try:
            # Step 1: Visit home page to get cookies
            response_home = session.get(url_home, timeout=10)
            if response_home.status_code != 200:
                raise Exception("NSE homepage access failed.")

            time.sleep(1.5)  # Wait to mimic human behavior

            # Step 2: Call Option Chain API with session
            response = session.get(url_api, timeout=10)
            response.raise_for_status()  # Raise error for bad responses

            return response.json()

        except Exception as e:
            st.warning(f"Retry {i+1}/{retries} failed: {e}")
            time.sleep(2)

    raise Exception("❌ All retries failed. NSE API access blocked or modified.")

 

if st.button("🔄 Fetch Option Chain Data"):
    with st.spinner("🔄 Please wait... Fetching data from NSE"):
        try:
            oc_data = fetch_option_chain(symbol)

            expiry_dates = oc_data["records"]["expiryDates"]
            expiry_date = st.selectbox("Select Expiry Date", expiry_dates)
            underlying_value = oc_data["records"]["underlyingValue"]
            data = oc_data["records"]["data"]

            rows = []

            # Filter data for selected expiry
            filtered_data = [
                item for item in data
                if ("CE" in item and item["CE"].get("expiryDate") == expiry_date) or
                   ("PE" in item and item["PE"].get("expiryDate") == expiry_date)
            ]

            for item in filtered_data:
                strike = item.get("strikePrice")

                if "CE" in item and item["CE"].get("expiryDate") == expiry_date:
                    ce = item["CE"]
                    rows.append({
                        "Instrument Type": ce.get("instrumentType", "OPTIDX"),
                        "Expiry Date": ce.get("expiryDate", expiry_date),
                        "Option": "CE",
                        "Strike": strike,
                        "Open": ce.get("openPrice"),
                        "High": ce.get("highPrice"),
                        "Low": ce.get("lowPrice"),
                        "Close": ce.get("closePrice"),
                        "Prev. Close": ce.get("prevClose"),
                        "Last": ce.get("lastPrice"),
                        "Chng": ce.get("change"),
                        "%Chng": ce.get("pChange"),
                        "Volume (Contracts)": ce.get("numberOfContractsTraded"),
                        "Value (₹ Lakhs)": ce.get("totalTradedVolume"),
                        "Ask Price": ce.get("askPrice"),
                        "Ask Qty": ce.get("askQty"),
                        "Bid Price": ce.get("bidPrice"),  # ✅ Fixed key
                        "Bid Qty": ce.get("bidQty"),
                        "Change in Open Interest": ce.get("changeinOpenInterest"),
                        "% Change in OI": ce.get("pchangeinOpenInterest"),
                        "Implied Volatility": ce.get("impliedVolatility"),
                        "Open Interest": ce.get("openInterest"),
                        "Total Buy Quantity": ce.get("totalBuyQuantity"),
                        "Total Sell Quantity": ce.get("totalSellQuantity"),
                        "Underlying Value": underlying_value
                    })

                if "PE" in item and item["PE"].get("expiryDate") == expiry_date:
                    pe = item["PE"]
                    rows.append({
                        "Instrument Type": pe.get("instrumentType", "OPTIDX"),
                        "Expiry Date": pe.get("expiryDate", expiry_date),
                        "Option": "PE",
                        "Strike": strike,
                        "Open": pe.get("openPrice"),
                        "High": pe.get("highPrice"),
                        "Low": pe.get("lowPrice"),
                        "Close": pe.get("closePrice"),
                        "Prev. Close": pe.get("prevClose"),
                        "Last": pe.get("lastPrice"),
                        "Chng": pe.get("change"),
                        "%Chng": pe.get("pChange"),
                        "Volume (Contracts)": pe.get("numberOfContractsTraded"),
                        "Value (₹ Lakhs)": pe.get("totalTradedVolume"),
                        "Ask Price": pe.get("askPrice"),
                        "Ask Qty": pe.get("askQty"),
                        "Bid Price": pe.get("bidPrice"),  # ✅ Fixed key
                        "Bid Qty": pe.get("bidQty"),
                        "Change in Open Interest": pe.get("changeinOpenInterest"),
                        "% Change in OI": pe.get("pchangeinOpenInterest"),
                        "Implied Volatility": pe.get("impliedVolatility"),
                        "Open Interest": pe.get("openInterest"),
                        "Total Buy Quantity": pe.get("totalBuyQuantity"),
                        "Total Sell Quantity": pe.get("totalSellQuantity"),
                        "Underlying Value": underlying_value
                    })

            df = pd.DataFrame(rows)
            df = df.dropna(subset=["Strike"]).sort_values(by=["Strike", "Option"])

            st.success("✅ Option Chain Data Fetched")
            st.subheader(f"📅 Expiry Date: {expiry_date} | 💰 Underlying Value: {underlying_value}")
            st.dataframe(df, use_container_width=True)

            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button("⬇️ Download CSV", csv, file_name="nifty_option_chain_full.csv", mime="text/csv")

        except Exception as e:
            st.error(f"❌ Error: {e}")
