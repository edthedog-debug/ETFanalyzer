# ETF Forecasting Dashboard

A lightweight, automated web dashboard that tracks historical closing prices and generates 30-day price forecasts using linear trends and machine learning approximations for the **Amundi MSCI Europe Growth UCITS ETF Acc**.

---

## 🚀 Features

* **Real-Time Data Integration:** Automatically fetches historical closing prices using `yfinance`.
* **30-Day Projections:** Displays simulated forecasting trends using ARIMA and Machine Learning models (LightGBM/XGBoost approximations).
* **Interactive Charts:** Powered by **Chart.js** to visualize historical performance alongside future price projections.
* **Bilingual Support:** Switch instantly between **English** and **Spanish**.
* **Automated Workflow:** Uses GitHub Actions to daily fetch new market data and update the repository seamlessly.

---

## 🛠️ Project Structure

```text
├── index.html            # Frontend dashboard interface
├── update_data.py        # Python script to download and process market data
├── market_data.json      # Generated JSON payload containing prices and forecasts
└── .github/
    └── workflows/
        └── update.yml    # GitHub Actions configuration for daily automation
