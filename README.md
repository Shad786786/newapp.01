# stock.app
 
 
 # 📊 Nifty 125 Dashboard — Stock, PFC, and Option Chain Viewer
 
  # LIVE DEMO: https://newapp01-c3aiym4rjvfvdj4jdkmxuv.streamlit.app/

This is a comprehensive Streamlit-based dashboard that allows users to:

- 🔍 Fetch and download **Nifty 125** stock data (Single Day or Full Month)
- 📉 Track **Power Finance Corporation Ltd. (PFC)** historical stock performance
- 📈 View full **Nifty Option Chain** with Open Interest (OI), Implied Volatility (IV), Bid/Ask, and more

---

## 🚀 Features

### 📌 Nifty 125 Stock Data
- Select between:
  - **Single Day Mode**: Choose Today, Yesterday, or Custom Date
  - **Full Month Mode**: Select any month and year
- Fetches OHLCV (Open, High, Low, Close, Volume) using `yfinance`
- Download data as CSV

### 📉 Power Finance Corporation Ltd. (PFC) Data
- Input custom **start and end date**
- Fetches daily historical data for PFC (including ISIN)
- Download data as CSV

### 📈 Nifty Option Chain Viewer
- Fetches data directly from **NSE India** using custom session + headers
- Includes full CE and PE chain with:
  - Strike price
  - Volume, Open Interest, IV, Bid/Ask, % Change in OI
- Filter by expiry date
- Download full chain as CSV

---

## 🛠 Technology Stack

- [Streamlit](https://streamlit.io/) – for UI
- [yfinance](https://pypi.org/project/yfinance/) – for historical stock data
- [nsepython](https://github.com/vaishnavsm/nsepython) + `requests` – for Option Chain scraping
- `pandas`, `datetime` – for data handling

---

## ▶️ How to Run

1. **Clone this repository:**
   ```bash
   git clone https://github.com/yourusername/nifty-125-dashboard.git
   cd nifty-125-dashboard
   
2. Install dependencies:
pip install -r requirements.txt

3. Run the Streamlit app:
streamlit run app.py


# 📌Sample Output

✅ Nifty 125 table with daily/monthly OHLCV

✅ Power Finance Corp data with ISIN

✅ Nifty Option Chain with expiry selector and strike-wise data



# 📄 License
This project is open-source and available under the MIT License.



# 🙌 Contributions
Pull requests and suggestions are welcome. If you'd like to add charts, multi-symbol option chains, or sector-wise filtering — feel free to fork and enhance!



#💬 Contact
Created by [SHAD] — [zadahmad321@gmail.com]
Feel free to connect or reach out for feedback!
