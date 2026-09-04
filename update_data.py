import json
from datetime import datetime, timezone
import yfinance as yf

# Definición de los ETFs con sus tickers correspondientes
etfs = {
    "LU1681042435": {
        "name": "Amundi MSCI Europe Growth UCITS ETF Acc",
        "ticker": "CG9.PA",
    },
    "IE00B4K48X80": {
        "name": "iShares Core MSCI Europe UCITS ETF (Acc)",
        "ticker": "IMAE.AS",
    },
}

data_output = {}

for isin, info in etfs.items():
    print(f"Descargando datos para {isin} ({info['ticker']})...")
    ticker_obj = yf.Ticker(info["ticker"])
    hist = ticker_obj.history(period="1mo")

    date_labels = []
    historical_prices = []

    for date, row in hist.iterrows():
        date_str = date.strftime("%Y-%m-%d")
        price = round(float(row["Close"]), 2)
        date_labels.append(date_str)
        historical_prices.append(price)

    # Último cierre registrado
    last_close = historical_prices[-1] if historical_prices else 0
    last_date = date_labels[-1] if date_labels else ""

    # Generar proyecciones simuladas (ARIMA / ML) basadas en el último precio
    forecast_days = 30
    forecast_labels = []
    arima_prices = []
    ml_prices = []

    current_date_obj = datetime.strptime(last_date, "%Y-%m-%d") if last_date else datetime.now()

    import math
    for i in range(1, forecast_days + 1):
        from datetime import timedelta
        current_date_obj += timedelta(days=1)
        forecast_labels.append(current_date_obj.strftime("%Y-%m-%d"))
        
        arima_val = round(last_close + (i * (last_close * 0.0004)) + math.sin(i * 0.3) * (last_close * 0.002), 2)
        ml_val = round(last_close + (i * (last_close * 0.0006)) + math.cos(i * 0.4) * (last_close * 0.003), 2)
        
        arima_prices.append(arima_val)
        ml_prices.append(ml_val)

    data_output[isin] = {
        "name": info["name"],
        "ticker": info["ticker"],
        "dateLabels": date_labels,
        "historicalPrices": historical_prices,
        "forecastLabels": forecast_labels,
        "arimaPrices": arima_prices,
        "mlPrices": ml_prices,
        "lastClose": last_close,
        "lastDate": last_date
    }

# Metadatos globales de actualización (UTC)
now_utc = datetime.now(timezone.utc)
payload = {
    "lastUpdateTimestamp": now_utc.isoformat(),
    "nextUpdateTimestamp": datetime.combine(now_utc.date() + timedelta(days=1), datetime.min.time(), tzinfo=timezone.utc).isoformat(), # Programado para el día siguiente
    "etfs": data_output
}

with open("market_data.json", "w", encoding="utf-8") as f:
    json.dump(payload, f, ensure_ascii=False, indent=4)

print("Archivo market_data.json generado con éxito.")